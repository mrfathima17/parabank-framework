import json
from pages.register_page import RegisterPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_register_new_user(page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    register = RegisterPage(page)
    register.register(data["register_user"])
    page.wait_for_timeout(3000)
    content = page.locator("#rightPanel").text_content()
    assert "Your account was created successfully" in content

def test_register_existing_username(page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    register = RegisterPage(page)
    register.register(data["existing_user"])
    page.wait_for_timeout(3000)
    content = page.locator("#rightPanel").text_content()
    assert "This username already exists" in content or \
           "taken" in content or \
           "already" in content.lower()

def test_register_mismatched_passwords(page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    register = RegisterPage(page)
    register.register_with_mismatched_password(
        data["register_user"],
        "WrongConfirm123"
    )
    page.wait_for_timeout(2000)
    assert page.url.__contains__("register")