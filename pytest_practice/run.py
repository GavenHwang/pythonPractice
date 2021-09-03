from datetime import datetime
from pathlib import Path

import pytest

if __name__ == '__main__':
    cwd = Path.cwd()
    # file_name = cwd.joinpath("test_ordering.py")
    # file_name = cwd.joinpath("test_assert.py")
    pytest.main([
        "-vs",
        "--html", "report/report_%s.html" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "--self-contained-html",
        "--log-file=report/pytest_%s.log" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "--capture=sys",
        "test_assert.py",
    ])