from pytest_bdd import scenario
from .contact_steps import *

@scenario('contacts.feature', 'Add new contact')
def test_add_contact():
    pass


@scenario('contacts.feature', 'Del random contact')
def test_del_contact():
    pass


@scenario('contacts.feature', 'Edit random contact')
def test_edit_contact():
    pass