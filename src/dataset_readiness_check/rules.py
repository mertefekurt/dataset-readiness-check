from __future__ import annotations

from dataset_readiness_check.models import Rule

PROJECT_NAME = 'dataset-readiness-check'
DESCRIPTION = 'Review ML dataset manifests for split, leakage, label, and consent readiness.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'labels unknown train only consent missing leakage possible'
MEDIUM_SAMPLE = '\\b(train only|no validation|no test split|split missing)\\b'
CLEAN_SAMPLE = 'train validation test splits documented labels reviewed consent recorded'

RULES = (
    Rule(
        code='missing-consent',
        severity='high',
        pattern='\\b(consent missing|license unknown|usage rights unknown)\\b',
        message='dataset usage rights are unclear',
        recommendation='Document license, consent, or approved usage basis.',
    ),
    Rule(
        code='missing-split',
        severity='medium',
        pattern='\\b(train only|no validation|no test split|split missing)\\b',
        message='dataset split is incomplete',
        recommendation='Create train, validation, and test splits.',
    ),
    Rule(
        code='label-uncertainty',
        severity='low',
        pattern='\\b(labels unknown|unreviewed labels|weak labels)\\b',
        message='label quality is uncertain',
        recommendation='Record labeling method and review sample quality.',
    ),
)
