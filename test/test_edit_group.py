# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group1(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test1'))
    app.group.edit_first_group(Group(name="edit", header="group", footer="form"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    app.group.edit_first_group(Group(name="new group"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(footer='test3'))
    app.group.edit_first_group(Group(header="new header"))

