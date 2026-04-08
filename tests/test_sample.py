import re
from playwright.sync_api import expect
def test_google_title(page):
    page.goto("https://www.google.com/ncr")
    try:
        page.get_to_role("button", name="I agree").click(timeout=3000)
    except:
        print("No popup")
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))