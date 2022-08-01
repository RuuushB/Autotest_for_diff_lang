from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_busket(browser):
    browser.get(link)
    x = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert x, "No such element found"
