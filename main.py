import os
from pathlib import Path

LINE = "Latency fixed: my canary deploy promoted the 404 page to 100%—2ms p99 beat checkout—so I deprecated you as a legacy client for still expecting HTTP 200."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
