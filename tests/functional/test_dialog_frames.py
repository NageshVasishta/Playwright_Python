from playwright.sync_api import Page, expect


def test_dialog_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", lambda s:s.accept())
    page.get_by_placeholder("Enter Your Name").fill("Nagesh")
    page.get_by_text("Confirm").click()

    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


def test_iframe_handle(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    frame = page.frame_locator("#courses-iframe")
    with page.expect_popup() as popup:
        frame.get_by_text("Check my Portfolio").click()
        new_page = popup.value

        expect(new_page).to_have_url("https://qasummit.org/about-speaker")
        expect(new_page.locator("h1")).to_contain_text("Rahul Shetty")
        new_page.close()

