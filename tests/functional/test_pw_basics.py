import re
import time

from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import browser


def test_valid_login_chrome(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.set_viewport_size({"width":1920,"height":1080})
    expect (page).to_have_title(re.compile("LoginPage Practise.*"))

    page.get_by_role("textbox", name="username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.locator("span:has-text('User')").click()
    page.locator("#okayBtn").click()
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").check()
    expect(page.get_by_role("checkbox")).to_be_checked()
    page.get_by_role("button", name="Sign In").click()
    expect(page).to_have_url(re.compile(".*/angularpractice/shop"))
    expect(page).to_have_title("ProtoCommerce")

def test_invalid_login_firefox(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width":1920,"height":1080})
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_role("textbox", name="username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("invalid")
    page.locator("span:has-text('User')").click()
    page.locator("#okayBtn").click()
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").check()
    expect(page.get_by_role("checkbox")).to_be_checked()
    time.sleep(3)
    page.get_by_role("button", name="Sign In").click()
    expect(page.locator(".alert-danger")).to_be_visible()
    expect(page.locator(".alert-danger")).to_have_text("Incorrect username/password.")
    expect(page).to_have_url(re.compile(".*loginpagePractise/"))

