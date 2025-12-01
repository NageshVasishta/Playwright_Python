import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="email@example.com").press("Tab")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("h3")).to_contain_text("Automation")
    expect(page.get_by_role("heading", name="Automation")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
