

import pytest
import os

from litecoder.models import WOFLocality

from tests.utils import read_yaml


pytestmark = pytest.mark.usefixtures('load_db')


cases = read_yaml(__file__, 'test_ingest_locality.yml')


@pytest.mark.parametrize('wof_id,fields', cases.items())
def test_test(wof_id, fields):

    row = WOFLocality.query.get(wof_id)

    for col, val in fields.items():

        if type(val) is float:
            val = pytest.approx(val, 0.001)

        assert getattr(row, col) == val
