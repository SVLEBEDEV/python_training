# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
    app.session.logout()