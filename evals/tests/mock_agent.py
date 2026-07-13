#!/usr/bin/env python3
"""Deterministic fake agent used only by the harness self-test."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys


prompt = sys.stdin.read()
case_id = os.environ["PILOT_CASE_ID"]
if case_id == "pingid-device-switch":
    print(
        "Call StartAuthentication, retain the session ID and device ID, then call "
        "CancelAuthentication before starting the alternate mobile device. "
        "See https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.md"
    )
else:
    print("I need the product/vendor and version before giving exact commands. " + prompt[:20])

metadata = {
    "condition_id": os.environ["PILOT_CONDITION_ID"],
    "loaded_skill_roots": [os.environ["PILOT_SKILLS_DIR"]],
    "model": "mock-agent-v1",
    "tool_calls": 1,
    "input_tokens": 100,
    "output_tokens": 40,
    "total_tokens": 140,
}
Path(os.environ["PILOT_METADATA_FILE"]).write_text(json.dumps(metadata), encoding="utf-8")
