class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Нажимаем кнопку создания группы
        wd.find_element_by_name("new").click()
        # Заполняем поля
        self.form_filling(group)
        # Поджтверждаем создание группы
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def form_filling(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name('delete').click()
        self.return_to_group_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name('edit').click()
        self.form_filling(group)
        wd.find_element_by_name('update').click()
        self.return_to_group_page()