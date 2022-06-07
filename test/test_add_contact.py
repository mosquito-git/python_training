# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact1(app, json_contacts):
    cont = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(cont)
    app.contact.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

