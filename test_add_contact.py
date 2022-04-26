# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import unittest
import contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.add_new_contact_click(wd)
        self.fill_name(wd, contact.FillName(firstname="aaaaa", middlename="bbbbb", lastname="ssssss", nickname="hhhhhhhh"))
        self.fill_company_fields(wd, contact.FillCompanyFields(title="ddddddd", company="lsrhlrhg", address="kshfu"))
        self.fill_telephone_fields(wd, contact.FillTelephoneFields(home="812-555-44-33", mobile="+7-935-777-88-99", work="567-78-99", fax="990-76-56"))
        self.fill_email_fields(wd, contact.FillEmailFields(email="ckckc@mail.ru", email2="wewe@mail2.ru", email3="wewrdd@mail3.ru", homepage="www.hfhfhf.ru"))
        self.fill_birthday_fields(wd, contact.FillBirthdayFields(bday="10", bmonth="May", byear="2000", aday="3", amonth="April", ayear="1999"))
        self.fill_secondary_fields(wd, contact.FillSecondaryFields(address2="sib", phone2="www.home2.ru", notes="notesnotesnotes"))
        self.submit_click(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def fill_secondary_fields(self, wd, secondaryfields):
        # fill address #2
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(secondaryfields.address2)
        # phone #2
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(secondaryfields.phone2)
        # notes
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(secondaryfields.notes)

    def fill_birthday_fields(self, wd, birthdayfields):
        # fill birthday
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(birthdayfields.bday)
        wd.find_element(By.CSS_SELECTOR, f'select[name="bday"] > option[value="{birthdayfields.bday}"]').click()
        # bmonth
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(birthdayfields.bmonth)
        wd.find_element(By.CSS_SELECTOR, f'select[name="bmonth"] > option[value="{birthdayfields.bmonth}"]').click()
        # byear
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(birthdayfields.byear)
        # aday
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(birthdayfields.aday)
        wd.find_element(By.CSS_SELECTOR, f'select[name="aday"] > option[value="{birthdayfields.aday}"]').click()
        # amonth
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(birthdayfields.amonth)
        wd.find_element(By.CSS_SELECTOR, f'select[name="amonth"] > option[value="{birthdayfields.amonth}"]').click()
        # ayear
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(birthdayfields.ayear)

    def fill_email_fields(self, wd, emailfields):
        # fill email#1
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(emailfields.email)
        # email #2
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(emailfields.email2)
        # email #3
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(emailfields.email3)
        # fill site homepage
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(emailfields.homepage)

    def fill_telephone_fields(self, wd, telfields):
        # fill home
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(telfields.home)
        # fill mobile tel
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(telfields.mobile)
        # fill work tel
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(telfields.work)
        # fill fax
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(telfields.fax)

    def fill_company_fields(self, wd, companyfields):
        # fill title
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(companyfields.title)
        # fill company name
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(companyfields.company)
        # fill company address
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(companyfields.address)

    def fill_name(self, wd, fillname):
        # fill name
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(fillname.firstname)
        # fill middlename
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(fillname.middlename)
        # fill lastname
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(fillname.lastname)
        # fill nickname
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(fillname.nickname)

    def add_new_contact_click(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd, username, password):
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://127.0.0.1/addressbook/")

    def submit_click(self, wd):
        wd.find_element(By.NAME, "submit").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
