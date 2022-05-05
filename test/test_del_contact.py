from model import contact


def test_del_contact1(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="gggggg", middlename="dfdfdf", lastname="dfffff"))
    app.contact.delete_first_contact()
