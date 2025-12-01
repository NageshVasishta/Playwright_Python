import re
import time

from playwright.sync_api import Playwright,expect,Page
products = ["iphone X","Blackberry","Nokia Edge","Samsung Note 8"]

def test_login_and_checkout(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login(page)
    for p in products:
        page.locator("app-card").filter(has_text= p).get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator("tbody tr .media")).to_have_count(len(products))

    raw = page.locator("tbody h3").nth(-1).text_content()
    print("raw price repr:", repr(raw))  # debug exact characters
    amount = re.sub(r'\D', '', raw or '')  # remove all non-digits
    print(f"Total price of the products is {amount}")

    page.get_by_role("button",name="Checkout").click()
    page.locator("#country").fill("India")
    page.locator("label[for='checkbox2']").click()
    page.locator("input[value='Purchase']").click()
    expect(page.locator(".alert-success")).to_contain_text("Success! Thank you! Your order will be delivered in next few weeks :-).")





def login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.set_viewport_size({"width": 1920, "height": 1080})
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

