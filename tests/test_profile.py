import json
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_update_profile(page):
    login = LoginPage(page)
    profile = ProfilePage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    profile.go_to_profile(page)
    page.wait_for_timeout(2000)
    profile.update_profile(data["update_profile"])
    page.wait_for_timeout(2000)
    assert "updated" in profile.get_success_message()