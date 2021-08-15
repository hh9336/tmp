import sys

import pytest

print(sys.path.append('..'))
from mark_po.page.ui import UI


@pytest.fixture(scope='session')
def start_class():
    ui = UI()
    com = ui.start()
    yield com
