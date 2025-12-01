import re
import time

from playwright.sync_api import Page, expect


def test_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as popup:
        page.locator("#openwindow").click()
        new_window = popup.value

        expect(new_window).to_have_url("https://www.qaclickacademy.com/")
        expect(new_window).to_have_title(re.compile(".*QAClick Academy"))
        new_window.close()

    page.bring_to_front()
    page.close()


def test_tab_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as popup:
        page.locator("#opentab").click()
        new_tab= popup.value
        new_tab.set_viewport_size({"width":1920,"height":1020})
        expect(new_tab).to_have_url("https://www.qaclickacademy.com/")
        expect(new_tab).to_have_title(re.compile(".*QAClick Academy"))
        new_tab.close()

    page.close()