# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_edit_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_group = Group(name="edit")
    edit_group.id = group.id
    app.group.edit_by_id(edit_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = edit_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)