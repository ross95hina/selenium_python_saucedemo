import time
from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import Main_page

def test_link_about():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.auhtorization()
    mp = Main_page(driver)
    mp.select_menu_about()

    time.sleep(4)






