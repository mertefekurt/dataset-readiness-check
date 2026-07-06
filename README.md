# Dataset Readiness Check

![Dataset Readiness Check cover](assets/readme-cover.svg)

> Review ML dataset manifests for split, leakage, label, and consent readiness

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | dataset readiness |
| Command | `dataset-readiness-check` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-consent` | high | dataset usage rights are unclear |
| `missing-split` | medium | dataset split is incomplete |
| `label-uncertainty` | low | label quality is uncertain |

## Try it locally

```bash
python -m pip install -e ".[dev]"
dataset-readiness-check examples/sample.txt
dataset-readiness-check examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m dataset_readiness_check --help
```
