import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest import mark
import selenium
import pytest
from sqlalchemy import null


@mark.parametrize("username,password", [("locked_out_user", "secret_sauce"), ("standard_user", "secret_sauce"), ("Ferwis", "Encarnacion")])
def test_Login(username, password):
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    buscar_email = driver.find_element(by=By.ID, value="user-name")
    buscar_email.send_keys(username)

    buscar_password = driver.find_element(by=By.ID, value="password")
    buscar_password.send_keys(password)

    presionar_registro = driver.find_element(by=By.ID, value="login-button")
    presionar_registro.click()

    time.sleep(8)

    timee = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./Test_{timee}.png")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"



def test_AgregarCarrito():
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    buscar_email = driver.find_element(by=By.ID, value="user-name")
    buscar_email.send_keys("standard_user")

    buscar_password = driver.find_element(by=By.ID, value="password")
    buscar_password.send_keys("secret_sauce")

    presionar_registro = driver.find_element(by=By.ID, value="login-button")
    presionar_registro.click()

    Agregar_Carrito = driver.find_element(by=By.XPATH, value="//*[@id='add-to-cart-sauce-labs-backpack']")
    Agregar_Carrito.click()

    time.sleep(8)

    timee = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./Test_{timee}.png")

    assert driver.find_element(by=By.XPATH, value="//*[@id='remove-sauce-labs-backpack']")


def test_VerCarrito():
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    buscar_email = driver.find_element(by=By.ID, value="user-name")
    buscar_email.send_keys("standard_user")

    buscar_password = driver.find_element(by=By.ID, value="password")
    buscar_password.send_keys("secret_sauce")

    presionar_registro = driver.find_element(by=By.ID, value="login-button")
    presionar_registro.click()

    Agregar_Carrito = driver.find_element(by=By.XPATH, value="//*[@id='add-to-cart-sauce-labs-backpack']")
    Agregar_Carrito.click()

    Ver_Carrito = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
    Ver_Carrito.click()

    time.sleep(8)

    timee = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./Test_{timee}.png")

    assert driver.current_url == "https://www.saucedemo.com/cart.html"




def test_Abrir_Menuu():
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    buscar_email = driver.find_element(by=By.ID, value="user-name")
    buscar_email.send_keys("standard_user")

    buscar_password = driver.find_element(by=By.ID, value="password")
    buscar_password.send_keys("secret_sauce")

    presionar_registro = driver.find_element(by=By.ID, value="login-button")
    presionar_registro.click()

    Agregar_Carrito = driver.find_element(by=By.XPATH, value="//*[@id='add-to-cart-sauce-labs-backpack']")
    Agregar_Carrito.click()

    Ver_Menu = driver.find_element(by=By.XPATH, value="//*[@id='react-burger-menu-btn']")
    Ver_Menu.click()

    time.sleep(8)

    timee = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./Test_{timee}.png")

    def assertTrue(param):
        pass
    assert assertTrue(Ver_Menu.get(3).getAttribute("aria-hidden") != null);


def test_Logout():
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    buscar_email = driver.find_element(by=By.ID, value="user-name")
    buscar_email.send_keys("standard_user")

    buscar_password = driver.find_element(by=By.ID, value="password")
    buscar_password.send_keys("secret_sauce")

    presionar_registro = driver.find_element(by=By.ID, value="login-button")
    presionar_registro.click()

    Ver_Menu = driver.find_element(by=By.XPATH, value="//*[@id='react-burger-menu-btn']")
    Ver_Menu.click()

    Salir = driver.find_element(by=By.XPATH, value="//*[@id='logout_sidebar_link']")
    Salir.click()

    time.sleep(8)

    timee = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./Test_{timee}.png")


    assert driver.current_url != "https://www.saucedemo.com/inventory.html"
