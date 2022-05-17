from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_date_field_value("bday", contact.bday)
        self.change_date_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_date_field_value("aday", contact.aday)
        self.change_date_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.home)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_date_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # click add new contact
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit click
        wd.find_element(By.NAME, "submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # check first contact and click
        wd.find_element(By.NAME, "selected[]").click()
        # click delete button
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        # xpath = // input[ @ value = 'Delete']
        # accept deletion
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # check first contact
        wd.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]').click()
        # click href edit
        wd.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        # update button click
        # wd.find_element(By.NAME, "update").click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"][name="update"]').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements(By.CSS_SELECTOR, 'input[type="button"][value="Send e-Mail"]')) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]'))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]'):
            td = element.find_elements(By.CSS_SELECTOR, 'td')
            # print('lastname=',td[1].text)
            # print('firstname=', td[2].text)
            id = element.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]').get_attribute(
                "value")
            # print("id=", id)
            contacts.append(Contact(firstname=td[2].text, lastname=td[1].text, id=id))
        return contacts
