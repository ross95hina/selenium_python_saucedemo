import time

import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=2)
def test_buy_product1():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.auhtorization()
    mp = Main_page(driver)
    mp.select_product1()
    cp = Cart_page(driver)
    cp.product_confirmation()
    cip = Client_information_page(driver)
    cip.input_information()
    p = Payment_page(driver)
    p.payment()
    f = Finish_page(driver)
    f.finish()
    time.sleep(4)


@pytest.mark.run(order=1)
def test_buy_product2():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.auhtorization()
    mp = Main_page(driver)
    mp.select_product2()
    cp = Cart_page(driver)
    cp.product_confirmation()
    cip = Client_information_page(driver)
    cip.input_information()
    p = Payment_page(driver)
    p.payment()
    f = Finish_page(driver)
    f.finish()
    time.sleep(4)

@pytest.mark.run(order=4)
def test_buy_product3():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.auhtorization()
    mp = Main_page(driver)
    mp.select_product3()
    cp = Cart_page(driver)
    cp.product_confirmation()
    cip = Client_information_page(driver)
    cip.input_information()
    p = Payment_page(driver)
    p.payment()
    f = Finish_page(driver)
    f.finish()
    time.sleep(4)

@pytest.mark.run(order=3)
def test_buy_product4():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.auhtorization()
    mp = Main_page(driver)
    mp.select_product4()
    cp = Cart_page(driver)
    cp.product_confirmation()
    cip = Client_information_page(driver)
    cip.input_information()
    p = Payment_page(driver)
    p.payment()
    f = Finish_page(driver)
    f.finish()
    time.sleep(4)






