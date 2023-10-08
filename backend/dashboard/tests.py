# Create your tests here.
from datetime import datetime, timedelta

import pytest

from dashboard.exceptions import InvalidInputException
from dashboard.utils import get_date_range


def test_date_range_period():
    date_range, period = get_date_range({'time_period': '7_days'})
    assert period == 'days'


def test_date_range_values():
    date_range, period = get_date_range({'time_period': '7_days'})
    end_range = datetime.now()
    start_range = end_range - timedelta(days=7)
    assert start_range.strftime('YYYY-MM-DD HH:MM') == date_range[0].strftime(
        'YYYY-MM-DD HH:MM') and end_range.strftime('YYYY-MM-DD HH:MM') == date_range[1].strftime('YYYY-MM-DD HH:MM')


class ColumnCreateError:
    pass


def test_date_range_invalid_inputs():
    with pytest.raises(InvalidInputException) as exc_info:
        date_range, period = get_date_range({})
    exc_info.match("Please provide valid input.")
