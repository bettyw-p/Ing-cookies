from playwright.sync_api import Page

class CookieBanner:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "ING Bank Śląski"
        self.customize_button = page.locator("//button[contains(text(), 'Dostosuj')]")
        self.accept_selected = page.locator("//button[contains(text(), 'Zaakceptuj zaznaczone')]")
        self.analytical_toggle = page.locator('[role="switch"][name="CpmAnalyticalOption"]')

    def get_toggle_state(self, toggle_type):
        return toggle_type.get_attribute("aria-checked")