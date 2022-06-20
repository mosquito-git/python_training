# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
# from fixture.orm import ORMFixture
# import re
import random


def test_del_contact_from_group1(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", middlename="dfdfdf", lastname=""))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="super", header="puper", footer="grp"))
    grp = random.choice(orm.get_group_list())
    # print('grp_list = ', grp)
    cont = random.choice(orm.get_contacts_not_in_group(Group(id=grp.id)))
    app.contact.add_to_group2(grp, cont)
    app.contact.click_group_page(grp)
    app.contact.select_contact_on_group_page_and_del2(cont)
    assert cont not in orm.get_contacts_in_group(Group(id=grp.id))
    assert cont in orm.get_contacts_not_in_group(Group(id=grp.id))

