import allure

from src.pages.registration_page import RegistrationPage
from src.data import users


#TODO относительные пути


@allure.label("owner", "lankinma")
@allure.story("Тестовая стори")
@allure.feature("Тестовая фича")
def test_practice_form(setup_browser):
    page = RegistrationPage()
    page.open()
    page.register(users.test_user)
    page.should_have_user(users.test_user)
