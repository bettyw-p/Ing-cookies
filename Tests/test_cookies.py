from playwright.sync_api import Page, expect
from pages.cookie_banner import CookieBanner
from config import BASE_URL

def test_accept_cookies(page: Page):
    cookie_banner = CookieBanner(page)
    page.goto(BASE_URL)
    cookie_banner.customize_button.click()

    state = cookie_banner.get_toggle_state(cookie_banner.analytical_toggle)

    if state == "false":
        cookie_banner.analytical_toggle.click()
    else:
        pass

    state = cookie_banner.get_toggle_state(cookie_banner.analytical_toggle)

    expect(cookie_banner.analytical_toggle).to_be_checked()

    cookie_banner.accept_selected.click()

    expect(page).to_have_title(cookie_banner.page_title)
    expect(cookie_banner.accept_selected).to_be_hidden()