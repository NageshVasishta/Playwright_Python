from http.cookiejar import offset_from_tz_string
from logging import NullHandler
from typing import Collection

from playwright.sync_api import Page,expect

def test_webtable_handle(page :Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with page.expect_popup() as popup:
        page.get_by_role('link', name="Top Deals").click()
        offer_page = popup.value
        offer_page.set_viewport_size({"width":1920, "height":1020})

        for index in range(offer_page.locator("table th").count()):
            if(offer_page.locator("table th")).nth(index).filter(has_text="Price").count()>0:
                    break
        price = offer_page.locator("table tr").filter(has_text="Rice").locator("td").nth(index).text_content()
        print(f"Price of rice is {price}")
        offer_page.close()
    page.close()


def test_capture_all_row_discounted_price(page:Page):
    item_dict = {}
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with page.expect_popup() as popup:
        page.get_by_role('link', name="Top Deals").click()
        new_page = popup.value
        col = None
        new_page.wait_for_selector("thead th")

        # for index in range(new_page.locator("thead th").count()):
        #     if (new_page.locator("thead th").nth(index).filter(has_text="Discount price").count())>0:
        #         col = index
        #         break
        headers = new_page.locator("thead th")
        for i in range(headers.count()):
            header_text = headers.nth(i).inner_text().strip().lower()
            if "discount" in header_text:
                col = i
                break

        assert col is not None, "Discount price column not found!:"

        for row in new_page.locator("tbody tr").all():
            name = row.locator("td").first.text_content()
            dp = row.locator("td").nth(col).text_content()
            item_dict[name] = dp

        new_page.close()
    page.close()

    for key, value in item_dict.items():
        print(f"Discounted price of {key} is {value}")