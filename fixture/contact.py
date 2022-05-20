from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # click delete button
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        # xpath = // input[ @ value = 'Delete']
        # accept deletion
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        print("index in select_contact_by_index=", index)
        # wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]')[index].click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        print("index in edit_cont_by_index=", index)
        # check first contact
        # wd.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]').click()
        # wd.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]')[index].click()
        self.select_contact_by_index(index)
        # click href edit
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Edit"]')[index].click()
        self.fill_contact_form(contact)
        # update button click
        # wd.find_element(By.NAME, "update").click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"][name="update"]').click()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]'):
                td = element.find_elements(By.CSS_SELECTOR, 'td')
                # print('lastname=',td[1].text)
                # print('firstname=', td[2].text)
                id = element.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]').get_attribute(
                    "value")
                # print("id=", id)
                all_phones = td[5].text
                address = td[3].text
                emails_td = td[4]
                all_emails_selen = emails_td.find_elements(By.CSS_SELECTOR, 'a')
                all_emails = list(map(lambda x: x.text, all_emails_selen))
                self.contact_cache.append(Contact(firstname=td[2].text, lastname=td[1].text, id=id,
                                                  address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[7]
        cell.find_element(By.TAG_NAME, 'a').click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(By.TAG_NAME, 'a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        homephone = wd.find_element(By.NAME, 'home').get_attribute('value')
        mobilephone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        workphone = wd.find_element(By.NAME, 'work').get_attribute('value')
        phone2 = wd.find_element(By.NAME, 'phone2').get_attribute('value')
        address = wd.find_element(By.CSS_SELECTOR, 'textarea[name="address"]').text
        email = wd.find_element(By.CSS_SELECTOR, 'input[name="email"]').get_attribute('value')
        email2 = wd.find_element(By.CSS_SELECTOR, 'input[name="email2"]').get_attribute('value')
        email3 = wd.find_element(By.CSS_SELECTOR, 'input[name="email3"]').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, home=homephone, mobile=mobilephone,
                       work=workphone, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element(By.ID, 'content').text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone,
                       work=workphone, phone2=phone2)
