# -*- coding: utf-8 -*-
import allure
import data
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step('Получаем список групп из БД'):
        old_groups = db.get_group_list()
    with allure.step('Создаем новую группу %s' % group):
        app.group.create(group)
    with allure.step('Получаем новый список групп из БД'):
        new_groups = db.get_group_list()
    old_groups.append(group)
    with allure.step('Проверяем, что группа в БД добавлена'):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        with allure.step('Проверяем, что группа на UI добавлена'):
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)