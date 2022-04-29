# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group1(app):
    app.group.edit_first_group(Group(name="edit", header="group", footer="form"))


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="new group"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="new header"))

