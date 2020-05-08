# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first(Contact(First_name="EDIT", Birthday_day="15"))