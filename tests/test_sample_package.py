import re

from sample_package import sample_package


def test_main(capsys):
    sample_package.main()
    captured = capsys.readouterr()
    assert re.match(r"^Hello from sample_package at .{7,8}.$", captured.out)
