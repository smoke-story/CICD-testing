from playwright.sync_api import Page, expect
import allure

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.button_login = page.locator("#login")
        self.error_alert = page.locator("#errorAlert")
        self.error_message = "Invalid credentials. Please try again."

    
    @allure.step("Открытие страницы авторизации")
    def open(self):
        self.page.goto("https://zimaev.github.io/pom/")

    @allure.step("Авторизация пользователя")
    def login_user(self, login: str, password: str):
        self.username_input.fill(login)
        self.password_input.fill(password)
        self.button_login.click()

    @allure.step("Проверка сообщения об ошибке входа")
    def check_alert_message(self):
        expect(self.error_alert).to_have_text(self.error_message)




