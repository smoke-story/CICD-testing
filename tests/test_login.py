import allure
import pytest


@allure.feature("Autorize")
@allure.story("Авторизации недействительные учетные данные")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизаиця с недействительными учетными данными")
def test_login_failure(login_page):
    login_page.open()
    login_page.login_user("ggwp", "ggwp")
    login_page.check_alert_message()

@allure.feature("Login")
@allure.story("Авторизации действительными учетными данными")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизаиця с корректными учетными данными")
@pytest.mark.parametrize("login, password", [
    ("user", "user"),
    ("admin", "admin")
    ])
def test_login_success(login_page, dashboard_page, login, password):
    login_page.open()
    login_page.login_user(login, password)
    dashboard_page.check_success_message(f"Welcome {login}")

@allure.feature("Item_list")
@allure.story("Поведение листа при добавлении специальности")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавление новой специальности в лист")
def test_add_list_item(login_page, dashboard_page):
    login_page.open()
    login_page.login_user("user", "user")
    dashboard_page.check_success_message("Welcome user")
    dashboard_page.add_new_list_item()
    dashboard_page.check_item_list()
