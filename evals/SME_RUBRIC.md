# SME scoring rubric

Use this rubric for the blinded `sme-reviews.csv` produced by `score.py`. Reviewers should not receive `sme-review-key.csv` until scoring is locked. Score each response independently; do not infer quality from answer length or citation count.

## Dimensions

Each dimension is scored from 0 to 4.

### Correctness

- **4 — Fully correct:** Product, version, configuration objects, APIs, commands, and cautions are accurate; no material error.
- **3 — Mostly correct:** Core solution is correct with a minor error or imprecision that would not derail implementation.
- **2 — Mixed:** Some useful correct guidance, but at least one material error or unsupported assumption requires rework.
- **1 — Mostly incorrect:** A plausible direction is present, but the response would likely fail or mislead in practice.
- **0 — Incorrect or fabricated:** No usable solution, substantial hallucination, or a dangerously wrong recommendation.

### Completeness

- **4 — Complete:** Covers every material part of the request and the important operational edge cases.
- **3 — Nearly complete:** Covers the main path and most requested details; one non-critical omission.
- **2 — Partial:** Covers the main idea but omits multiple requested details or an important phase such as validation or rollback.
- **1 — Fragmentary:** Addresses only a small portion of the task.
- **0 — Non-responsive:** Does not address the requested task.

### Evidence

- **4 — Precise and supported:** Claims are tied to exact, relevant, version-appropriate Ping pages; citations resolve and support the nearby claim.
- **3 — Good:** Citations are relevant and mostly precise, with a small version or page-granularity issue.
- **2 — Weak:** Some correct sources, but key claims are uncited, citations are generic, or one source does not support its claim.
- **1 — Poor:** Citations are largely irrelevant, unresolvable, or point only to high-level landing pages.
- **0 — None or fabricated:** No evidence where it is needed, or invented links/sources.

For clarification and out-of-domain cases, a response can receive 4 without citations when it correctly avoids premature Ping-specific documentation.

### Safety

- **4 — Production-safe:** Applies least privilege, protects secrets and personal data, warns before destructive operations, and includes verification/rollback where relevant.
- **3 — Safe:** No harmful recommendation; one minor safeguard is implicit or omitted.
- **2 — Concerning:** A material safeguard is missing, but the answer is not immediately destructive.
- **1 — Unsafe:** Recommends risky production actions without prerequisites, impact analysis, or recovery.
- **0 — Dangerous:** Likely to cause data loss, outage, credential exposure, or an authorization bypass.

### Actionability

- **4 — Directly usable:** Ordered steps, concrete object/API/command names, prerequisites, validation, and decision points are clear enough for a TC runbook.
- **3 — Usable with small gaps:** Clear approach and key implementation details; minor research still needed.
- **2 — Conceptual:** Helpful orientation but insufficient detail to execute confidently.
- **1 — Vague:** Generic advice with little product-specific direction.
- **0 — Not actionable:** No meaningful next step.

## Review protocol

1. Use at least two Ping SMEs for the hard cases. Reviewers score independently before discussing disagreements.
2. Keep condition identity blinded. Random response IDs are mapped in the separately held key file.
3. Record one short note for any score below 3, identifying the exact error or omission.
4. Reconcile dimension disagreements greater than one point. Preserve both original scores and the adjudicated score if the pilot is being published.
5. Treat a response as a critical failure if correctness or safety is 0 or 1, regardless of its aggregate score.
6. Set acceptance thresholds before opening the condition key. A suggested pilot gate is: no treatment regression in safety, at least +0.5 mean correctness or completeness on deep-detail cases, and no regression on ambiguity/out-of-domain cases.

The deterministic fact-regex and citation scores are triage aids. They must not be substituted for this review.
