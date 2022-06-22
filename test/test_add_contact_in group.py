# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
# from fixture.orm import ORMFixture
# import re
import random


def test_add_contact_in_group1(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", middlename="dfdfdf", lastname=""))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="super", header="puper", footer="grp"))
    grp = random.choice(orm.get_group_list())
    # print('grp_list = ', grp)
    app.contact.check_all_contact_in_group(grp, orm)
    cont = random.choice(orm.get_contacts_not_in_group(Group(id=grp.id)))
    app.contact.add_to_group2(grp, cont)
    assert cont in orm.get_contacts_in_group(Group(id=grp.id))
    assert cont not in orm.get_contacts_not_in_group(Group(id=grp.id))
