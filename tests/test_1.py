from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser


def test_1(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_2(playwright : Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.groww.in')