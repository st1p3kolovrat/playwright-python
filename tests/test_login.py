from playwright.sync_api import expect
from data.data import UserCredentials, ErrorMsg
from conftest import BASE_URL


def test_standard_user_login(page, login_page):
    login_page.login(UserCredentials.STANDARD_USER, UserCredentials.PASSWORD)
    expect(page).to_have_url(f"{BASE_URL}inventory.html")


def test_locked_out_user_login(login_page):
    login_page.login(UserCredentials.LOCKED_OUT_USER, UserCredentials.PASSWORD)
    expect(login_page.error_msg).to_have_text(ErrorMsg.LOGIN_ERR_LOCKED_OUT)


def test_delayed_user_login(page, login_page, inventory_page):
    login_page.login(UserCredentials.PERFORMANCE_GLITCH_USER, UserCredentials.PASSWORD)
    page.wait_for_url(f"{BASE_URL}inventory.html")
    expect(inventory_page.inventory_container).to_be_visible()


def test_login_with_invalid_username(login_page):
    login_page.login("invalid123", UserCredentials.PASSWORD)
    expect(login_page.error_msg).to_have_text(ErrorMsg.LOGIN_ERR_INVALID_CREDS)


def test_login_with_invalid_pwd(login_page):
    login_page.login(UserCredentials.STANDARD_USER, "invalid!pwd123")
    expect(login_page.error_msg).to_have_text(ErrorMsg.LOGIN_ERR_INVALID_CREDS)


def test_login_with_username_missing(login_page):
    login_page.login("", UserCredentials.PASSWORD)
    expect(login_page.error_msg).to_have_text(ErrorMsg.LOGIN_ERR_USERNAME_MISSING)


def test_login_with_pwd_missing(login_page):
    login_page.login(UserCredentials.STANDARD_USER, "")
    expect(login_page.error_msg).to_have_text(ErrorMsg.LOGIN_ERR_PWD_MISSING)
