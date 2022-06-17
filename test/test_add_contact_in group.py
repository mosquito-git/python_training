# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import re



def test_add_contact_in_group1(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", middlename="dfdfdf", lastname=""))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="super", header="puper", footer="grp"))
    # print(list(db_orm.get_contacts_in_group))
    # if len(db_orm.get_contacts_in_group)
    # print('cnt=', db.count_contacts_in_group())
    if db.count_contacts_in_group() == 0:
        grp_to_check = app.contact.add_to_group()
        print('grp_to_check=', grp_to_check)
        contacts_from_grp_cont_page = sorted(app.contact.get_grp_cont_page(grp_to_check), key=Contact.id_or_max)
        contacts_from_grp_cont_db = sorted(orm.get_contacts_in_group(Group(id=grp_to_check)), key=Contact.id_or_max)


    else:
        grp_id = db.get_group_id_in_contacts_in_group()
        print('grp_id = ', grp_id)
        contacts_from_grp_cont_page = sorted(app.contact.get_grp_cont_page(grp_id), key=Contact.id_or_max)
        contacts_from_grp_cont_db = sorted(orm.get_contacts_in_group(Group(id=grp_id)), key=Contact.id_or_max)

    for i in range(len(contacts_from_grp_cont_db)):
        assert contacts_from_grp_cont_page[i].firstname == contacts_from_grp_cont_db[i].firstname
        assert contacts_from_grp_cont_page[i].lastname == contacts_from_grp_cont_db[i].lastname
        assert contacts_from_grp_cont_page[i].address == contacts_from_grp_cont_db[i].address
        assert merge_phones_like_on_home_page(contacts_from_grp_cont_page[i]) == merge_phones_like_on_home_page(
            contacts_from_grp_cont_db[i])
        assert merge_emails(contacts_from_grp_cont_page[i].all_emails_from_home_page) == merge_emails(
            [contacts_from_grp_cont_db[i].email, contacts_from_grp_cont_db[i].email2,
             contacts_from_grp_cont_db[i].email3])


def clear(s):
    return re.sub("[+() -/]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home,
                                                                                                        contact.mobile,
                                                                                                        contact.work,
                                                                                                        contact.phone2]))))


def merge_emails(emails):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, emails))))
