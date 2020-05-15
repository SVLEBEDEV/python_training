# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)