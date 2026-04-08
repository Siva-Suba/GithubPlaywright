import re
from playwright.sync_api import Page, expect
from pages.Orangehrm_login_page import LoginPage
from pages.Orangehrm_home_page import HomePage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    page.get_by_role("link", name="Performance").click()
    page.get_by_role("link", name="Dashboard").click()
    
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page.login("Admin", "admin123")
    login_page.click_login()
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
    
