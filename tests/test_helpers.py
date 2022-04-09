import re

from sample_package import helpers


def test_get_current_time():
    time_string = helpers.get_current_time()
    assert re.match(r"^\d{1,2}:\d{2} (A|P)M$", time_string)
