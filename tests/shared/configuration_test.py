from unittest import mock

import pytest

from shared import configuration
from shared.exceptions import InvalidArgumentException

# TODO add tests with
# * tmpdir/etc to test reading/writing functionality
# * os.environ
# * _load and _dump


# TODO patch _load instead
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data='{"foo":"bar"}')
def test_get(mock_file):
    with mock.patch.object(configuration, "DEFAULTS", {}):
        assert configuration.get("foo") == "bar"


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="{}")
def test_get_default(mock_file):
    with mock.patch.object(configuration, "DEFAULTS", {"foo": "bar"}):
        assert configuration.get("foo") == "bar"


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="{}")
def test_get_nonexistent(mock_file):
    with mock.patch.object(configuration, "DEFAULTS", {}):
        with pytest.raises(InvalidArgumentException) as e:
            configuration.get("foo")
            assert "foo" in e
