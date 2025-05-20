from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_bike_light_btn = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.add_to_cart_jacket_btn = page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        self.remove_from_cart_jacket_btn = page.locator('[data-test="remove-sauce-labs-fleece-jacket"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.inventory_container = page.locator('[id="inventory_container"]').first

    def add_to_cart_bike_light(self):
        self.add_to_cart_bike_light_btn.click()

    def add_to_cart_jacket(self):
        self.add_to_cart_jacket_btn.click()

    def remove_from_cart_jacket(self):
        self.remove_from_cart_jacket_btn.click()
