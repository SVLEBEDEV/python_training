# -*- coding: utf-8 -*-


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()