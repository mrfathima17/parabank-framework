import json
from pages.login_page import LoginPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_valid_login(page):
    login = LoginPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    assert login.is_logged_in()

def test_invalid_login(page):
    login = LoginPage(page)
    login.login(
        data["invalid_user"]["username"],
        data["invalid_user"]["password"]
    )
    page.wait_for_selector("#rightPanel p.error")
    assert "could not be verified" in login.get_error_message()

def test_logout(page):
    login = LoginPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    login.logout()
    assert not login.is_logged_in()

def test_empty_username(page):
    login = LoginPage(page)
    login.login("", data["valid_user"]["password"])
    assert not login.is_logged_in()

def test_empty_password(page):
    login = LoginPage(page)
    login.login(data["valid_user"]["username"], "")
    assert not login.is_logged_in()

def test_both_fields_empty(page):
    login = LoginPage(page)
    login.login("", "")
    assert not login.is_logged_in()