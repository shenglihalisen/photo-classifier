import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from tests.helpers import cleanup_temp_files


@pytest.fixture(autouse=True)
def auto_cleanup_temp_files():
    yield
    cleanup_temp_files()
