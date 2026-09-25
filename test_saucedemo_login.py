from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage
chrome_options = Options()
chrome_options.add_argument("--disable-features=PasswordLeakDetection")
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}
chrome_options.add_experimental_option("prefs", prefs)
def test_successful_login():
    driver = webdriver.Chrome(options=chrome_options)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    driver.quit()


def test_locked_out_login():
    driver = webdriver.Chrome(options=chrome_options)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    error_message = driver.find_element("css selector", "[data-test='error']").text
    assert "Sorry, this user has been locked out" in error_message
    driver.quit()


def test_checkout_flow():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "shopping_cart_container").click()
    driver.find_element("id", "checkout").click()

    driver.find_element("id", "first-name").send_keys("Abel")
    driver.find_element("id", "last-name").send_keys("Adhanom")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "finish").click()

    confirmation = driver.find_element("class name", "complete-header").text
    assert "Thank you for your order" in confirmation

    driver.quit()


def test_reset_app_state():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    driver.find_element("id", "react-burger-menu-btn").click()
    driver.find_element("id", "reset_sidebar_link").click()

    cart_badges = driver.find_elements("class name", "shopping_cart_badge")
    assert len(cart_badges) == 0

    driver.quit()


from selenium.webdriver.support.ui import Select
def test_sort_price_low_to_high():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    sort_dropdown = Select(driver.find_element("class name", "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")

    price_elements = driver.find_elements("class name", "inventory_item_price")
    prices = []
    for price_element in price_elements:
        price_text = price_element.text.replace("$", "")
        prices.append(float(price_text))

    assert prices == sorted(prices)

    driver.quit()