# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.add_new_contact_click(wd)
        self.fill_name(wd)
        self.fill_company_fields(wd)
        self.fill_telephone_fields(wd)
        self.fill_email_fields(wd)
        self.fill_birthday_fields(wd)
        self.fill_secondary_fields(wd)
        self.submit_click(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def fill_secondary_fields(self, wd):
        # fill address #2
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys("msk")
        # phone #2
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys("www.hhhhhh.com")
        # notes
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys("hkhjhkjhlku")

    def fill_birthday_fields(self, wd):
        # fill birthday
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("13")
        wd.find_element(By.CSS_SELECTOR, 'select[name="bday"] > option[value="13"]').click()
        # bmonth
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("December")
        wd.find_element(By.CSS_SELECTOR, 'select[name="bmonth"] > option[value="December"]').click()
        # byear
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys("2013")
        # aday
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("15")
        wd.find_element(By.CSS_SELECTOR, 'select[name="aday"] > option[value="15"]').click()
        # amonth
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("August")
        wd.find_element(By.CSS_SELECTOR, 'select[name="amonth"] > option[value="August"]').click()
        # ayear
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys("1990")

    def fill_email_fields(self, wd):
        # fill email#1
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys("ecetfrfr@gmail.com")
        # email #2
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys("adewda@yandex.ru")
        # email #3
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys("decd@mail.ru")
        # fill site homepage
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys("www.hello.ru")

    def fill_telephone_fields(self, wd):
        # fill home
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys("spb")
        # fill mobile tel
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys("+71239999999")
        # fill work tel
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys("8678998")
        # fill fax
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys("3456789")

    def fill_company_fields(self, wd):
        # fill title
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("dfdfdfdff")
        # fill company name
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys("dadadda")
        # fill company address
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys("spb")

    def fill_name(self, wd):
        # fill name
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("aaaaaaa")
        # fill middlename
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("bbbbbbbb")
        # fill lastname
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("ccccccc")
        # fill nickname
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("erererer")

    def add_new_contact_click(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd):
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
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
