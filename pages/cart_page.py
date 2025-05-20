from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_link = page.locator('[id="shopping_cart_container"]')
        self.checkout_btn = page.get_by_role("button", name="Checkout")
        self.continue_btn = page.get_by_role("button", name="Continue")
        self.finish_btn = page.get_by_role("button", name="Finish")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.header_title = page.locator('[data-test="title"]')
        self.complete_header = page.locator('[data-test="complete-header"]')

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def go_to_checkout(self):
        self.checkout_btn.click()

    def fill_your__information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_btn.click()

    def verify_page_title(self, title: str):
        expect(self.header_title).to_have_text(title)

    def finish_order(self):
        self.finish_btn.click()
