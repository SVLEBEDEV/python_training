from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0:
            return
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.form_filling(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def form_filling(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.First_name)
        self.change_field_value('middlename', contact.Middle_name)
        self.change_field_value('lastname', contact.Last_name)
        self.change_field_value('nickname', contact.Nickname)
        self.change_field_value('title', contact.Title)
        self.change_field_value('company', contact.Company)
        self.change_field_value('address', contact.Address)
        self.change_field_value('home', contact.Home)
        self.change_field_value('mobile', contact.Mobile)
        self.change_field_value('work', contact.Work)
        self.change_field_value('fax', contact.Fax)
        self.change_field_value('email', contact.E_mail)
        self.change_field_value('email2', contact.E_mail2)
        self.change_field_value('email3', contact.E_mail3)
        self.change_field_value('homepage', contact.Fax)
        self.change_field_value('fax', contact.Homepage)
        self.change_field_value_list('bday', contact.Birthday_day)
        self.change_field_value_list('bmonth', contact.Birthday_month)
        self.change_field_value('byear', contact.Birthday_year)
        self.change_field_value_list('aday', contact.Anniversary_day)
        self.change_field_value_list('amonth', contact.Anniversary_month)
        self.change_field_value('ayear', contact.Anniversary_year)
        self.change_field_value('address2', contact.Address_Secondary)
        self.change_field_value('phone2', contact.Home_Secondary)
        self.change_field_value('notes', contact.Notes)

    def change_field_value_list(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0:
            return
        wd.find_element_by_link_text("add new").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def edit_first(self, new_group_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first()
        wd.find_element_by_xpath('//img[@alt="Edit"]').click()
        self.form_filling(new_group_data)
        wd.find_element_by_name('update').click()
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))