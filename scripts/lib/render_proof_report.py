#!/usr/bin/env python3
"""Render validation and routing proof output as a static HTML report."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape
import os
from pathlib import Path
import subprocess

from ping_docsets import load_docsets
from routing_proof import SAMPLES, Sample, SkillRoute, route_question


@dataclass(frozen=True)
class CommandResult:
    label: str
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def run_command(label: str, command: tuple[str, ...], repo_root: Path) -> CommandResult:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=repo_root,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return CommandResult(
        label=label,
        command=command,
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )


def shell_command(command: tuple[str, ...]) -> str:
    return " ".join(command)


def status_text(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def status_class(ok: bool) -> str:
    return "pass" if ok else "fail"


def short_url(url: str, limit: int = 82) -> str:
    if len(url) <= limit:
        return url
    return url[: limit - 1].rstrip("/") + "..."


def command_block(result: CommandResult) -> str:
    output = result.stdout
    if result.stderr:
        output = f"{output}\n\nSTDERR:\n{result.stderr}" if output else result.stderr
    if not output:
        output = "(no output)"
    return f"""
      <details class="command" open>
        <summary>
          <span>{escape(result.label)}</span>
          <b class="{status_class(result.ok)}">{status_text(result.ok)}</b>
        </summary>
        <div class="command-meta">
          <code>{escape(shell_command(result.command))}</code>
          <span>exit {result.returncode}</span>
        </div>
        <pre>{escape(output)}</pre>
      </details>
    """


def route_pass(sample: Sample, route: SkillRoute) -> bool:
    return (
        route.docset.skill_slug == sample.expected_skill
        and route.guide.guide == sample.expected_guide
        and (route.snapshot == "live-only" or bool(route.snapshot))
    )


def route_card(sample: Sample, route: SkillRoute) -> str:
    ok = route_pass(sample, route)
    skill_terms = ", ".join(route.matched_skill_terms) or "none"
    guide_terms = ", ".join(route.matched_guide_terms) or "none"
    entry_terms = ", ".join(route.matched_entry_terms) or "none"
    return f"""
      <article class="route-case">
        <header class="case-head">
          <div>
            <p class="eyebrow">{escape(sample.name)}</p>
            <h3>{escape(route.docset.label)}</h3>
          </div>
          <span class="badge {status_class(ok)}">{status_text(ok)}</span>
        </header>

        <p class="question">{escape(sample.question)}</p>

        <div class="route-lane" aria-label="Routing lane for {escape(sample.name)}">
          <div class="node source">
            <span>Question</span>
            <strong>Product intent</strong>
            <small>terms: {escape(skill_terms)}</small>
          </div>
          <div class="connector" aria-hidden="true"></div>
          <div class="node skill">
            <span>Skill</span>
            <strong>{escape(route.docset.skill_slug)}</strong>
            <small>score {route.skill_score}</small>
          </div>
          <div class="connector" aria-hidden="true"></div>
          <div class="node index">
            <span>Index</span>
            <strong>references/llms.txt</strong>
            <small>online page discovery</small>
          </div>
          <div class="connector" aria-hidden="true"></div>
          <div class="node guide">
            <span>Guide</span>
            <strong>{escape(route.guide.guide)}</strong>
            <small>score {route.guide_score}; terms: {escape(guide_terms)}</small>
          </div>
          <div class="connector" aria-hidden="true"></div>
          <div class="node live">
            <span>Live first</span>
            <strong>{escape(short_url(route.entry.url))}</strong>
            <small>entry score {route.entry_score}; terms: {escape(entry_terms)}</small>
          </div>
          <div class="connector fallback" aria-hidden="true"></div>
          <div class="node fallback">
            <span>Fallback</span>
            <strong>{escape(route.snapshot)}</strong>
            <small>only if live fetch fails</small>
          </div>
        </div>

        <dl class="evidence">
          <div><dt>Expected skill</dt><dd>{escape(sample.expected_skill)}</dd></div>
          <div><dt>Expected guide</dt><dd>{escape(sample.expected_guide)}</dd></div>
          <div><dt>Live pattern</dt><dd><code>{escape(route.route_pattern)}</code></dd></div>
          <div><dt>Selected live URL</dt><dd><code>{escape(route.entry.url)}</code></dd></div>
          <div><dt>Fallback snapshot</dt><dd><code>{escape(route.snapshot)}</code></dd></div>
        </dl>
      </article>
    """


def render_report(
    repo_root: Path,
    output_path: Path,
    include_live_validation: bool,
) -> int:
    commands = [
        CommandResult(
            label="Route table and snapshot validation",
            command=(
                "scripts/validate.sh",
                "--skip-url-check",
                "--require-all-enabled",
            ),
            returncode=0,
            stdout="",
            stderr="",
        ),
        CommandResult(
            label="Routing proof assertions",
            command=("scripts/routing-proof.sh", "--assert-defaults"),
            returncode=0,
            stdout="",
            stderr="",
        ),
    ]

    command_results: list[CommandResult] = []
    for command in commands:
        command_results.append(run_command(command.label, command.command, repo_root))
    if include_live_validation:
        command_results.append(
            run_command(
                "Sampled live docs validation",
                (
                    "scripts/validate.sh",
                    "--require-all-enabled",
                    "--url-sample-percent",
                    "1",
                    "--url-sample-max",
                    "3",
                ),
                repo_root,
            )
        )

    routes = [
        (sample, route_question(sample.question, repo_root, "scripts/docsets.yaml", "plugins/ping-identity-docs/skills"))
        for sample in SAMPLES
    ]
    enabled_docsets = [
        docset for docset in load_docsets(repo_root / "scripts/docsets.yaml") if docset.enabled
    ]
    validation_ok = all(result.ok for result in command_results)
    route_ok = all(route_pass(sample, route) for sample, route in routes)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    html = html_document(
        generated_at=generated_at,
        validation_ok=validation_ok,
        route_ok=route_ok,
        enabled_count=len(enabled_docsets),
        command_results=command_results,
        routes=routes,
        include_live_validation=include_live_validation,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0 if validation_ok and route_ok else 1


def html_document(
    generated_at: str,
    validation_ok: bool,
    route_ok: bool,
    enabled_count: int,
    command_results: list[CommandResult],
    routes: list[tuple[Sample, SkillRoute]],
    include_live_validation: bool,
) -> str:
    command_html = "\n".join(command_block(result) for result in command_results)
    route_html = "\n".join(route_card(sample, route) for sample, route in routes)
    pass_count = sum(1 for result in command_results if result.ok)
    route_pass_count = sum(1 for sample, route in routes if route_pass(sample, route))
    live_label = "included" if include_live_validation else "skipped"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ping Agent Skills Routing Proof</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #111827;
      --muted: #5b6472;
      --line: #d8dee8;
      --surface: #f6f8fb;
      --panel: #ffffff;
      --accent: #0f766e;
      --accent-soft: #d9f4ef;
      --warn: #b42318;
      --warn-soft: #fee4e2;
      --code: #182230;
      --code-soft: #eef2f6;
      --shadow: 0 18px 45px rgba(17, 24, 39, 0.08);
    }}

    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background:
        linear-gradient(180deg, rgba(15, 118, 110, 0.08), transparent 360px),
        var(--surface);
      line-height: 1.5;
    }}
    a {{ color: inherit; }}
    .page {{ min-height: 100vh; }}
    .hero {{
      padding: 52px clamp(22px, 6vw, 92px) 36px;
      border-bottom: 1px solid var(--line);
      background:
        radial-gradient(circle at 84% 12%, rgba(15, 118, 110, 0.14), transparent 28%),
        linear-gradient(135deg, #ffffff 0%, #f3f7fa 62%, #edf3f2 100%);
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.55fr);
      gap: clamp(28px, 5vw, 72px);
      align-items: end;
      max-width: 1400px;
      margin: 0 auto;
    }}
    .brand {{
      margin: 0 0 18px;
      font-size: clamp(44px, 8vw, 106px);
      line-height: 0.9;
      letter-spacing: 0;
      max-width: 960px;
    }}
    .lede {{
      max-width: 760px;
      margin: 0;
      color: var(--muted);
      font-size: clamp(18px, 2.2vw, 25px);
    }}
    .summary-strip {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}
    .metric {{
      min-height: 112px;
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.78);
      box-shadow: var(--shadow);
    }}
    .metric span {{
      display: block;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .metric strong {{
      display: block;
      margin-top: 8px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1;
    }}
    main {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 34px clamp(18px, 4vw, 64px) 64px;
    }}
    section {{ margin-top: 42px; }}
    .section-head {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--line);
    }}
    h2 {{
      margin: 0;
      font-size: clamp(24px, 3vw, 42px);
      letter-spacing: 0;
    }}
    .section-head p {{
      margin: 0;
      color: var(--muted);
      max-width: 660px;
    }}
    .system-flow {{
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 12px;
      margin-top: 24px;
    }}
    .flow-step {{
      position: relative;
      min-height: 132px;
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      overflow: hidden;
    }}
    .flow-step::after {{
      content: "";
      position: absolute;
      inset: auto 18px 18px auto;
      width: 36px;
      height: 2px;
      background: var(--accent);
      opacity: 0.45;
    }}
    .flow-step span {{
      display: block;
      color: var(--accent);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .flow-step strong {{
      display: block;
      margin-top: 14px;
      font-size: 18px;
    }}
    .flow-step small {{
      display: block;
      margin-top: 8px;
      color: var(--muted);
    }}
    .validation-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
      margin-top: 24px;
    }}
    .status-panel {{
      padding: 20px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }}
    .status-panel b {{
      display: inline-flex;
      min-width: 74px;
      justify-content: center;
      padding: 5px 10px;
      border-radius: 999px;
      font-size: 12px;
      letter-spacing: 0.08em;
    }}
    .status-panel p {{
      margin: 14px 0 0;
      color: var(--muted);
    }}
    .pass {{
      color: #05603a;
      background: var(--accent-soft);
    }}
    .fail {{
      color: var(--warn);
      background: var(--warn-soft);
    }}
    .route-stack {{
      display: grid;
      gap: 22px;
      margin-top: 24px;
    }}
    .route-case {{
      padding: clamp(20px, 3vw, 32px);
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      box-shadow: var(--shadow);
      transition: transform 180ms ease, border-color 180ms ease;
    }}
    .route-case:hover {{
      transform: translateY(-2px);
      border-color: rgba(15, 118, 110, 0.42);
    }}
    .case-head {{
      display: flex;
      justify-content: space-between;
      gap: 18px;
      align-items: start;
    }}
    .eyebrow {{
      margin: 0 0 4px;
      color: var(--accent);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    h3 {{
      margin: 0;
      font-size: clamp(22px, 2.6vw, 34px);
      letter-spacing: 0;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 70px;
      border-radius: 999px;
      padding: 6px 12px;
      font-weight: 800;
      font-size: 12px;
      letter-spacing: 0.08em;
    }}
    .question {{
      margin: 18px 0 22px;
      max-width: 980px;
      color: var(--muted);
      font-size: 17px;
    }}
    .route-lane {{
      display: grid;
      grid-template-columns:
        minmax(150px, 0.95fr) 26px
        minmax(130px, 0.8fr) 26px
        minmax(160px, 1fr) 26px
        minmax(150px, 0.95fr) 26px
        minmax(220px, 1.35fr) 26px
        minmax(170px, 1fr);
      gap: 0;
      align-items: center;
      overflow-x: auto;
      padding: 6px 2px 16px;
    }}
    .node {{
      min-height: 126px;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: linear-gradient(180deg, #ffffff, #f9fbfc);
    }}
    .node span {{
      display: block;
      color: var(--accent);
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .node strong {{
      display: block;
      margin-top: 8px;
      overflow-wrap: anywhere;
      font-size: 15px;
      line-height: 1.28;
    }}
    .node small {{
      display: block;
      margin-top: 8px;
      color: var(--muted);
      overflow-wrap: anywhere;
    }}
    .node.live {{
      border-color: rgba(15, 118, 110, 0.38);
      background: linear-gradient(180deg, #f7fffd, #ffffff);
    }}
    .node.fallback {{
      border-style: dashed;
    }}
    .connector {{
      height: 2px;
      background: linear-gradient(90deg, var(--accent), rgba(15, 118, 110, 0.2));
      position: relative;
    }}
    .connector::after {{
      content: "";
      position: absolute;
      right: -1px;
      top: -4px;
      width: 0;
      height: 0;
      border-top: 5px solid transparent;
      border-bottom: 5px solid transparent;
      border-left: 7px solid var(--accent);
    }}
    .connector.fallback {{
      background: repeating-linear-gradient(90deg, var(--muted) 0 7px, transparent 7px 13px);
      opacity: 0.62;
    }}
    .connector.fallback::after {{ border-left-color: var(--muted); }}
    .evidence {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1px;
      margin: 22px 0 0;
      background: var(--line);
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
    }}
    .evidence div {{
      padding: 14px;
      background: #fbfcfe;
      min-width: 0;
    }}
    .evidence dt {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .evidence dd {{
      margin: 6px 0 0;
      overflow-wrap: anywhere;
    }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 0.92em;
      color: var(--code);
      background: var(--code-soft);
      padding: 2px 5px;
      border-radius: 5px;
    }}
    .command-list {{
      display: grid;
      gap: 12px;
      margin-top: 24px;
    }}
    details.command {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      overflow: hidden;
    }}
    details.command summary {{
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      padding: 16px 18px;
      font-weight: 800;
    }}
    details.command summary b {{
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 12px;
      letter-spacing: 0.08em;
    }}
    .command-meta {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      padding: 0 18px 14px;
      color: var(--muted);
      border-bottom: 1px solid var(--line);
    }}
    pre {{
      margin: 0;
      padding: 18px;
      overflow-x: auto;
      color: #dbe7ef;
      background: #111827;
      font-size: 13px;
      line-height: 1.55;
    }}
    .footer {{
      margin-top: 48px;
      padding-top: 20px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      display: flex;
      justify-content: space-between;
      gap: 18px;
      flex-wrap: wrap;
    }}
    @media (max-width: 1050px) {{
      .hero-grid,
      .validation-grid,
      .system-flow,
      .evidence {{
        grid-template-columns: 1fr;
      }}
      .summary-strip {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
    }}
    @media (max-width: 640px) {{
      .hero {{ padding: 34px 18px 28px; }}
      main {{ padding: 24px 16px 46px; }}
      .summary-strip {{ grid-template-columns: 1fr; }}
      .section-head {{ display: block; }}
      .section-head p {{ margin-top: 10px; }}
      .route-lane {{
        grid-template-columns: minmax(220px, 1fr);
        gap: 10px;
      }}
      .connector {{
        width: 2px;
        height: 22px;
        justify-self: center;
      }}
      .connector::after {{
        right: -4px;
        top: auto;
        bottom: -1px;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 7px solid var(--accent);
        border-bottom: 0;
      }}
      .connector.fallback::after {{
        border-top-color: var(--muted);
        border-left-color: transparent;
      }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="hero">
      <div class="hero-grid">
        <div>
          <h1 class="brand">Ping Agent Skills Routing Proof</h1>
          <p class="lede">Validation output and diagrammed route evidence for the online-first, snapshot-fallback documentation skills.</p>
        </div>
        <div class="summary-strip" aria-label="Report summary">
          <div class="metric"><span>Validation</span><strong>{status_text(validation_ok)}</strong></div>
          <div class="metric"><span>Routing</span><strong>{status_text(route_ok)}</strong></div>
          <div class="metric"><span>Skills checked</span><strong>{enabled_count}</strong></div>
          <div class="metric"><span>Live checks</span><strong>{escape(live_label)}</strong></div>
        </div>
      </div>
    </header>

    <main>
      <section>
        <div class="section-head">
          <h2>Architecture</h2>
          <p>The proof follows the same contract used by the generated skills: route by product skill, read the cached index, fetch live Markdown first, and use snapshots only as fallback.</p>
        </div>
        <div class="system-flow">
          <div class="flow-step"><span>1</span><strong>User question</strong><small>Product and task terms are extracted from the request.</small></div>
          <div class="flow-step"><span>2</span><strong>Skill selection</strong><small>The selected Ping product skill loads its instructions.</small></div>
          <div class="flow-step"><span>3</span><strong>llms.txt discovery</strong><small>The local index maps task language to official Markdown pages.</small></div>
          <div class="flow-step"><span>4</span><strong>Live documentation</strong><small>The selected online Markdown URL is the source of truth.</small></div>
          <div class="flow-step"><span>5</span><strong>Snapshot fallback</strong><small>The committed snapshot is used only if the live fetch is unavailable.</small></div>
        </div>
      </section>

      <section>
        <div class="section-head">
          <h2>Validation</h2>
          <p>These are actual command results generated for this report, not static screenshots.</p>
        </div>
        <div class="validation-grid">
          <div class="status-panel"><b class="{status_class(command_results[0].ok)}">{status_text(command_results[0].ok)}</b><p>Routing tables match the model derived from cached indexes, and all enabled skills are present.</p></div>
          <div class="status-panel"><b class="{status_class(command_results[1].ok)}">{status_text(command_results[1].ok)}</b><p>Representative complex questions route to the expected product skill and guide.</p></div>
          <div class="status-panel"><b class="{status_class(validation_ok)}">{pass_count}/{len(command_results)}</b><p>Command checks passed. Live validation is {escape(live_label)} for this report.</p></div>
        </div>
        <div class="command-list">
          {command_html}
        </div>
      </section>

      <section>
        <div class="section-head">
          <h2>Routing Proof</h2>
          <p>Each lane shows the decision chain from question to skill, guide, live Markdown URL, and fallback snapshot.</p>
        </div>
        <div class="validation-grid">
          <div class="status-panel"><b class="{status_class(route_ok)}">{route_pass_count}/{len(routes)}</b><p>Sample routes matched expected skill and guide.</p></div>
          <div class="status-panel"><b class="pass">LIVE</b><p>Selected URLs are online documentation routes from the cached Ping indexes.</p></div>
          <div class="status-panel"><b class="pass">FALLBACK</b><p>Every sample names the snapshot path used if live fetching fails.</p></div>
        </div>
        <div class="route-stack">
          {route_html}
        </div>
      </section>

      <footer class="footer">
        <span>Generated {escape(generated_at)}</span>
        <span>Source: scripts/render-proof-report.sh</span>
      </footer>
    </main>
  </div>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="reports/routing-proof.html",
        help="Path to write the HTML report, relative to repo root unless absolute.",
    )
    parser.add_argument(
        "--skip-live-validation",
        action="store_true",
        help="Skip sampled online Markdown URL validation when rendering the report.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = repo_root / output_path
    return render_report(
        repo_root=repo_root,
        output_path=output_path,
        include_live_validation=not args.skip_live_validation,
    )


if __name__ == "__main__":
    raise SystemExit(main())
