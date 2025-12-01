import re

from playwright.sync_api import Playwright, expect


def continue_request(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/abcdefgh")

def test_continue_request(playwright:Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("h3")).to_contain_text("Automation")
    expect(page.get_by_role("heading", name="Automation")).to_be_visible()

    page.get_by_text("ORDERS").click()

    page.route(re.compile(r".*/order/get-orders-details\?id=.*"), continue_request)

    page.get_by_role("button",name="View").nth(1).click()

    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")
    expect(page.locator(".blink_me")).to_have_css("color", "rgb(255, 0, 0)")
    page.screenshot(path = "screenshots/Unauthorized.png")
    page.close()