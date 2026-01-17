import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(driver, base_url):
    page = LoginPage(driver, base_url)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert page.loginButtonIsNotVisible()


@pytest.mark.regression
def test_login_failure(driver, base_url):
    page = LoginPage(driver, base_url)
    page.open()
    page.login("wrong_username", "secret_sauce")
    assert "Username and password do not match" in page.getErrorMessage()