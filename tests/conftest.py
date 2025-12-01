import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def launch_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
# # conftest.py
# import pytest
# from pathlib import Path
# from playwright.sync_api import Playwright, Browser, BrowserContext, Page
# import json, os
#
# # =====================================
# # Command line options
# # =====================================
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chromium",
#         help="Browser: chromium | firefox | webkit"
#     )
#     parser.addoption(
#         "--env", action="store", default="dev",
#         help="Environment: dev | qa | stg"
#     )
#
# # =====================================
# # Load environment config
# # (optional - for future use)
# # =====================================
# def load_env_config(env):
#     config_path = f"config/{env}.json"
#     if os.path.exists(config_path):
#         with open(config_path) as file:
#             return json.load(file)
#     return {}   # allow framework to run even if config not added yet
#
#
# @pytest.fixture(scope="session")
# def config(request):
#     env = request.config.getoption("--env")
#     return load_env_config(env)
#
#
# # =====================================
# # Launch Browser (session level)
# # =====================================
# @pytest.fixture(scope="session")
# def browser_instance(request, playwright: Playwright) -> Browser:
#     browser_name = request.config.getoption("--browser")
#
#     if browser_name == "chromium":
#         browser = playwright.chromium.launch(headless=False)
#     elif browser_name == "firefox":
#         browser = playwright.firefox.launch(headless=False)
#     elif browser_name == "webkit":
#         browser = playwright.webkit.launch(headless=False)
#     else:
#         raise ValueError(f"Invalid browser name: {browser_name}")
#
#     yield browser
#     browser.close()
#
#
# # =====================================
# # Page fixture (per test)
# # =====================================
# @pytest.fixture
# def page(browser_instance: Browser, config) -> Page:
#     context: BrowserContext = browser_instance.new_context()
#     page: Page = context.new_page()
#
#     # Optional timeout (for future environment config)
#     default_timeout = config.get("timeout", 5000)
#     page.set_default_timeout(default_timeout)
#
#     yield page
#
#     context.close()
#
#
# # =====================================
# # Screenshot on Failure
# # =====================================
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     if result.when == "call" and result.failed:
#         page_obj = item.funcargs.get("page", None)
#
#         if page_obj:
#             screenshot_dir = Path("reports/screenshots")
#             screenshot_dir.mkdir(parents=True, exist_ok=True)
#
#             test_name = item.name.replace("/", "_")
#             file_path = screenshot_dir / f"{test_name}.png"
#
#             page_obj.screenshot(path=str(file_path))
#             print(f"\n📸 Screenshot saved to: {file_path}\n")
