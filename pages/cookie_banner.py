from playwright.sync_api import Page

class CookieBanner:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "ING Bank Śląski"
        self.customize_button = page.locator("//button[contains(text(), 'Dostosuj')]")
        self.accept_selected = page.locator("//button[contains(text(), 'Zaakceptuj zaznaczone')]")
        self.dismiss_all = page.locator("//button[contains(@class,'js-cookie-policy-main-decline-button')]")
        self.accept_all = page.locator("//button[contains(text(), 'Zaakceptuj wszystkie')]")
        self.analytical_toggle = page.locator('[role="switch"][name="CpmAnalyticalOption"]')
    
    def check_accepted_cookies(self, page: Page, expected_value):
        cookies = page.context.cookies()
        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        expected_value = expected_value
        actual_value = cookie_dict.get('cookiePolicyGDPR')
        assert actual_value == expected_value