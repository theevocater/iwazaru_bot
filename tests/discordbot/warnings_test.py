from unittest import mock

import pytest

from discordbot import warnings


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("foo", "gentle reminder: foo is bar"),
        ("asdf foo asdf", "gentle reminder: foo is bar"),
        ("fizz", None),
    ),
)
def test_simple_warning(text, expected):
    with mock.patch.object(warnings, "WARNINGS", {r"\b(foo)\b": "bar"}):
        assert warnings.parse_message(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("hey guys", warnings.GUYS_RESPONSE),
        ("Hi       gUys", warnings.GUYS_RESPONSE),
        ("guys", None),
    ),
)
def test_warning_guys(text, expected):
    assert warnings.parse_message(text) == expected
