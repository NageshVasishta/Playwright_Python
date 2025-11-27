import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def launch_browser(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    