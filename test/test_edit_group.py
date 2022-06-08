# -*- coding: utf-8 -*-

from model.group import Group
# from random import randrange
import random


# def test_edit_first_group1(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test1'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="edit", header="group", footer="form"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = db.get_group_list()
    group_rnd = random.choice(old_groups)
    idx = old_groups.index(group_rnd)
    group = Group(name="edit_edit_edit")
    group.id = group_rnd.id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        old_groups[idx] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer='test3'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="new header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

