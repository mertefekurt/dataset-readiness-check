![Dataset Readiness Check cover](assets/readme-cover.svg)

# Dataset Readiness Check

> Review ML dataset manifests for split, leakage, label, and consent readiness

This is a review desk for dataset readiness. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `dataset-readiness-check`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `missing-consent` | high | dataset usage rights are unclear |
| `missing-split` | medium | dataset split is incomplete |
| `label-uncertainty` | low | label quality is uncertain |

## Try the sample

```bash
git clone https://github.com/mertefekurt/dataset-readiness-check.git
cd dataset-readiness-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
dataset-readiness-check examples/sample.txt
dataset-readiness-check examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
