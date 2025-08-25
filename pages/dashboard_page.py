from playwright.sync_api import Page, expect
import allure


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.success_message = page.locator("#usernameDisplay")
        self.add_button = page.locator("button[onclick='addItem()']")
        self.item_list = page.locator("#interactiveList li")
        

    @allure.step("Проверка сообщения об успешной авторизации")
    def check_success_message(self, login: str):
        expect(self.success_message).to_have_text(login)

    @allure.step("Добавление новой специальности в лист")
    def add_new_list_item(self):
        for i in range(50):
            self.add_button.scroll_into_view_if_needed()
            self.add_button.click()

    @allure.step("Проверка колличества специальностей в листе")
    def check_item_list(self):
        expect(self.item_list).to_have_count(53)
