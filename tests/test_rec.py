import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("playwright demo")
    page.get_by_text("playwright demo project", exact=True).click()
    page.locator("iframe[name=\"a-11e9kxv7n5mx\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click(timeout=5000)
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"0\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"3\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"7\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"2\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"12\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"12\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"9\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"6\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"10\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"9\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"9\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"6\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.locator("[id=\"10\"]").click()
    page.locator("iframe[name=\"c-11e9kxv7n5mx\"]").content_frame.get_by_role("button", name="Verify").click()
    page.get_by_role("link", name="playwright-demo · GitHub").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
