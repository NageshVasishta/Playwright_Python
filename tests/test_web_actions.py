from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser

from conftest import launch_page


def test_web_actions(launch_page):
    print("python")