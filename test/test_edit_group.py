# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit", header="group", footer="form"))
    app.session.logout()
