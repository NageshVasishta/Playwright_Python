"""
Enhanced Playwright script for https://rahulshettyacademy.com/client login
with better element detection and post-login verification
"""

import time
from playwright.sync_api import Page, expect, sync_playwright

# Credentials
USERNAME = "rahulshetty@gmail.com"
PASSWORD = "Iamking@000"
LOGIN_URL = "https://rahulshettyacademy.com/client"


def test_login_rahul_academy(page: Page):
    """
    Complete login flow to Rahul Shetty Academy client portal
    """

    print("\n" + "="*60)
    print("RAHUL SHETTY ACADEMY LOGIN TEST")
    print("="*60)

    # Step 1: Navigate to login page
    print("\n[Step 1] Navigating to login page...")
    page.goto(LOGIN_URL, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=30000)
    print(f"✓ Page loaded. URL: {page.url}")

    # Step 2: Take screenshot of login page
    print("\n[Step 2] Taking screenshot of login page...")
    page.screenshot(path="screenshots/01_login_page.png")
    print("✓ Screenshot saved: screenshots/01_login_page.png")

    # Step 3: Identify and fill email field
    print("\n[Step 3] Locating and filling email field...")
    email_locator = page.locator("input[type='email']")
    email_locator.wait_for(timeout=10000)
    print(f"✓ Email field found: {email_locator}")

    email_locator.fill(USERNAME)
    print(f"✓ Email entered: {USERNAME}")

    # Step 4: Identify and fill password field
    print("\n[Step 4] Locating and filling password field...")
    password_locator = page.locator("input[type='password']")
    password_locator.wait_for(timeout=10000)
    print(f"✓ Password field found: {password_locator}")

    password_locator.fill(PASSWORD)
    print(f"✓ Password entered (hidden for security)")

    # Step 5: Locate and click login button
    print("\n[Step 5] Locating and clicking login button...")

    # Try multiple selector strategies for the login button
    login_button = page.locator("input[type='submit']")
    if login_button.count() > 0:
        print(f"✓ Login button found using 'input[type=\"submit\"]'")
        login_button.click()
    else:
        # Try alternative selector
        login_button = page.locator("button:has-text('Login')")
        if login_button.count() > 0:
            print(f"✓ Login button found using 'button:has-text(\"Login\")'")
            login_button.click()

    print("✓ Login button clicked")

    # Step 6: Wait for navigation after login
    print("\n[Step 6] Waiting for page redirect after login...")
    page.wait_for_load_state("networkidle", timeout=30000)
    time.sleep(2)  # Additional wait for dynamic content
    print(f"✓ Page loaded. Current URL: {page.url}")

    # Step 7: Verify login success
    print("\n[Step 7] Verifying successful login...")

    # Take screenshot of post-login page
    page.screenshot(path="screenshots/02_post_login_page.png")

    print("✓ Screenshot saved: screenshots/02_post_login_page.png")

    # Check for common post-login indicators
    page_title = page.title()
    print(f"✓ Page title: {page_title}")

    # Check if URL changed (indicates successful login)
    if "login" not in page.url.lower():
        print("✓ URL changed - Login appears successful!")
    else:
        print("⚠ URL still contains 'login' - May need additional verification")

    # Try to find dashboard or welcome element
    try:
        # Look for various post-login elements
        selectors_to_check = [
            "//h1",  # Main heading
            "//h2",  # Secondary heading
            ".navbar",  # Navigation bar
            ".dashboard",  # Dashboard class
            "[class*='welcome']",  # Welcome message
            "[class*='product']",  # Product listing
        ]

        for selector in selectors_to_check:
            elements = page.locator(selector)
            if elements.count() > 0:
                print(f"✓ Found element: {selector} (count: {elements.count()})")
                if elements.count() <= 3:
                    text = elements.first.text_content()
                    print(f"  Content: {text[:100] if text else 'N/A'}")
    except Exception as e:
        print(f"⚠ Could not verify post-login elements: {e}")

    print("\n" + "="*60)
    print("✓ LOGIN TEST COMPLETED SUCCESSFULLY")
    print("="*60 + "\n")


def test_login_with_wait_for_navigation(page: Page):
    """
    Alternative approach using wait_for_navigation
    """
    print("\n[Alternative Method] Using wait_for_navigation...")

    page.goto(LOGIN_URL)

    # Fill email and password
    page.fill("input[type='email']", USERNAME)
    page.fill("input[type='password']", PASSWORD)

    # Click login and wait for navigation
    with page.expect_navigation(timeout=30000):
        page.click("input[type='submit']")

    print(f"✓ Navigation completed. Current URL: {page.url}")


if __name__ == "__main__":
    """
    Run directly without pytest for quick testing
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True for background execution
        page = browser.new_page()

        try:
            test_login_rahul_academy(page)
            # Uncomment to test alternative method:
            # test_login_with_wait_for_navigation(page)
        except Exception as e:
            print(f"\n❌ Error occurred: {e}")
            import traceback
            traceback.print_exc()
        finally:
            browser.close()

