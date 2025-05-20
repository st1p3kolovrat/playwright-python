import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        context.close()
        browser.close()


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)
