from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # fill middlename
        # wd.find_element(By.NAME, "middlename").click()
        # wd.find_element(By.NAME, "middlename").clear()
        # wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        # fill lastname
        # wd.find_element(By.NAME, "lastname").click()
        # wd.find_element(By.NAME, "lastname").clear()
        # wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        # fill nickname
        # wd.find_element(By.NAME, "nickname").click()
        # wd.find_element(By.NAME, "nickname").clear()
        # wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # fill title
        # in add/edit contact  swapped title,company,address
        # wd.find_element(By.NAME, "title").click()
        # wd.find_element(By.NAME, "title").clear()
        # wd.find_element(By.NAME, "title").send_keys(contact.title)
        # fill company name
        # wd.find_element(By.NAME, "company").click()
        # wd.find_element(By.NAME, "company").clear()
        # wd.find_element(By.NAME, "company").send_keys(contact.company)
        # fill company address
        # wd.find_element(By.NAME, "address").click()
        # wd.find_element(By.NAME, "address").clear()
        # wd.find_element(By.NAME, "address").send_keys(contact.address)
        # fill home
        # wd.find_element(By.NAME, "home").click()
        # wd.find_element(By.NAME, "home").clear()
        # wd.find_element(By.NAME, "home").send_keys(contact.home)
        # fill mobile tel
        # wd.find_element(By.NAME, "mobile").click()
        # wd.find_element(By.NAME, "mobile").clear()
        # wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        # fill work tel
        # wd.find_element(By.NAME, "work").click()
        # wd.find_element(By.NAME, "work").clear()
        # wd.find_element(By.NAME, "work").send_keys(contact.work)
        # fill fax
        # wd.find_element(By.NAME, "fax").click()
        # wd.find_element(By.NAME, "fax").clear()
        # wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        # fill email#1
        # wd.find_element(By.NAME, "email").click()
        # wd.find_element(By.NAME, "email").clear()
        # wd.find_element(By.NAME, "email").send_keys(contact.email)
        # email #2
        # wd.find_element(By.NAME, "email2").click()
        # wd.find_element(By.NAME, "email2").clear()
        # wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        # # email #3
        # wd.find_element(By.NAME, "email3").click()
        # wd.find_element(By.NAME, "email3").clear()
        # wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        # fill site homepage
        # wd.find_element(By.NAME, "homepage").click()
        # wd.find_element(By.NAME, "homepage").clear()
        # wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        # fill birthday
        # wd.find_element(By.NAME, "bday").click()
        # Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        # wd.find_element(By.CSS_SELECTOR, f'select[name="bday"] > option[value="{contact.bday}"]').click()
        # # bmonth
        # wd.find_element(By.NAME, "bmonth").click()
        # Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        # # wd.find_element(By.CSS_SELECTOR, f'select[name="bmonth"] > option[value="{contact.bmonth}"]').click()
        # # byear
        # # wd.find_element(By.NAME, "byear").click()
        # # wd.find_element(By.NAME, "byear").clear()
        # # wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        # # aday
        # wd.find_element(By.NAME, "aday").click()
        # Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        # # wd.find_element(By.CSS_SELECTOR, f'select[name="aday"] > option[value="{contact.aday}"]').click()
        # # amonth
        # wd.find_element(By.NAME, "amonth").click()
        # # contact add month value upper, contact edit month lower ! (contact.amonth.lower())
        # Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        # # wd.find_element(By.CSS_SELECTOR, f'select[name="amonth"] > option[value="{contact.amonth}"]').click()
        # ayear
        # wd.find_element(By.NAME, "ayear").click()
        # wd.find_element(By.NAME, "ayear").clear()
        # wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # fill address #2
        # wd.find_element(By.NAME, "address2").click()
        # wd.find_element(By.NAME, "address2").clear()
        # wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        # phone #2
        # wd.find_element(By.NAME, "phone2").click()
        # wd.find_element(By.NAME, "phone2").clear()
        # wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        # notes
        # wd.find_element(By.NAME, "notes").click()
        # wd.find_element(By.NAME, "notes").clear()
        # wd.find_element(By.NAME, "notes").send_keys(contact.notes)

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
        # self.fill_contact_fields(contact)
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
        # self.fill_contact_fields(contact)
        # update button click
        # wd.find_element(By.NAME, "update").click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"][name="update"]').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
