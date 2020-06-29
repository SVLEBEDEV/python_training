from pytest_bdd import scenario
from .group_steps import *

@scenario('groups.feature', 'Add new group')
def test_add_group():
    pass

@scenario('groups.feature', 'Del random group')
def test_del_group():
    pass