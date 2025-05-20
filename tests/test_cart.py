from playwright.sync_api import expect
from data.data import UserCredentials


def test_can_add_item_to_cart(login_page, inventory_page):
    login_page.login(UserCredentials.STANDARD_USER, UserCredentials.PASSWORD)
    inventory_page.add_to_cart_bike_light()
    expect(inventory_page.cart_badge).to_have_text("1")


def test_can_remove_one_item_from_the_cart(login_page, inventory_page):
    login_page.login(UserCredentials.STANDARD_USER, UserCredentials.PASSWORD)
    inventory_page.add_to_cart_bike_light()
    inventory_page.add_to_cart_jacket()
    expect(inventory_page.cart_badge).to_have_text("2")
    # Remove one item from the cart
    inventory_page.remove_from_cart_jacket()
    expect(inventory_page.cart_badge).to_have_text("1")


def test_can_make_successful_order(login_page, inventory_page, cart_page):
    login_page.login(UserCredentials.STANDARD_USER, UserCredentials.PASSWORD)
    inventory_page.add_to_cart_bike_light()
    cart_page.go_to_cart()
    cart_page.go_to_checkout()
    cart_page.fill_your__information(first_name="Pedro", last_name="Barbosa", postal_code="58000")
    cart_page.verify_page_title("Checkout: Overview")
    cart_page.finish_order()
    expect(cart_page.complete_header).to_have_text("Thank you for your order!")
