import re

from playwright.sync_api import Page, expect

def fulfill(route):
    return route.fulfill(json = {"data": [], "message": "No Orders"})


def test_fulfill_request(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("h3")).to_contain_text("Automation")
    expect(page.get_by_role("heading", name="Automation")).to_be_visible()

    page.route(re.compile(".*/ecom/order/get-orders-for-customer/.*"), fulfill)
    page.get_by_text("ORDERS").click()
    expect(page.get_by_text(" You have No Orders to show at this time.")).to_be_visible()
    page.screenshot(path="screenshots/empty_order_screen.png", full_page=True)

    page.close()
