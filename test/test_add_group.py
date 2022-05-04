# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group1(app):
    app.group.create(Group(name="dffdfdf", header="dfdfdfd", footer="dfdfdf"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

