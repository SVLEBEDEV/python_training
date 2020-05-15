# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_del_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups