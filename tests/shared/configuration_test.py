from unittest import mock

import pytest

from shared import configuration
from shared.exceptions import InvalidArgumentException


@mock.patch('builtins.open', new_callable=mock.mock_open, read_data='{}')
def test_get_default(mock_file):
    with mock.patch.object(configuration, 'DEFAULTS', {'foo': 'bar'}):
        assert configuration.get('foo') == 'bar'


@mock.patch('builtins.open', new_callable=mock.mock_open, read_data='{}')
def test_get_nonexistent(mock_file):
    with mock.patch.object(configuration, 'DEFAULTS', {}):
        with pytest.raises(InvalidArgumentException) as e:
            configuration.get('foo')
            assert 'foo' in e

# TODO add tests with tmpdir/etc to test reading/writing functionality
