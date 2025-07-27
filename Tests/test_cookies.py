from playwright.sync_api import Page, expect
import pytest
from pages.cookie_banner import CookieBanner
from config import BASE_URL, PAGE_TITLE

@pytest.fixture(autouse=True)
def go_to_base_url(page):
    page.goto(BASE_URL)
    expect(page).to_have_title(PAGE_TITLE)

@pytest.fixture
def cookie_banner(page: Page) -> CookieBanner:
    return CookieBanner(page)

def test_accept_analytics_cookies(page: Page, cookie_banner: CookieBanner):
    cookie_banner.customize_button.click()
    cookie_banner.analytical_toggle.click()
    expect(cookie_banner.analytical_toggle).to_be_checked()
    cookie_banner.accept_selected.click()
    expect(cookie_banner.accept_selected).to_be_hidden()
    cookie_banner.check_accepted_cookies(page, "3")

def test_dismiss_cookies(page: Page, cookie_banner: CookieBanner):
    cookie_banner.dismiss_all.click()
    expect(cookie_banner.dismiss_all).to_be_hidden()
    cookie_banner.check_accepted_cookies(page, "1")

def test_accept_all_cookies(page: Page, cookie_banner: CookieBanner):
    cookie_banner.accept_all.click()
    expect(cookie_banner.accept_all).to_be_hidden()
    cookie_banner.check_accepted_cookies(page, "4")