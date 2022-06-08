# from model import contact
from model.contact import Contact
import time
# from random import randrange
import random


def test_del_contact1(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="task20", middlename="del", lastname="contact"))
    # old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts))
    ## app.contact.delete_first_contact()
    # app.contact.delete_contact_by_index(index)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    # new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    ## old_contacts[0:1] = []
    # old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
