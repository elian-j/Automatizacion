import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def test_proyecto():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    def guardar_captura(driver, nombre_base):#metodo para que la foto tenga la fecha y hora
        os.makedirs("imagenes", exist_ok=True)
        timestamp = time.strftime("%Y-%m-%d%H-%M-%S")
        nombre_completo = f"imagenes/{nombre_base}{timestamp}.png"
        driver.save_screenshot(nombre_completo)



    time.sleep(10)


    textbox = driver.find_element(By.ID, "user-name")

    textbox.send_keys("standard_user")

    textbox = driver.find_element(By.ID, "password")

    textbox.send_keys("secret_sauce")

    guardar_captura(driver, "Foto1")

    time.sleep(5)

    button = driver.find_element(By.ID, "login-button")
    button.click()

    guardar_captura(driver, "")

    time.sleep(5)

    # #u_0_0_Ux
    button = driver.find_element(By.ID, "react-burger-menu-btn")
    button.click()
    guardar_captura(driver, "Foto2")
    time.sleep(5)
    # #u_0_6_f1
    button = driver.find_element(By.ID, "about_sidebar_link")
    button.click()
    guardar_captura(driver, "Foto3")
    time.sleep(5)
    button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button.click()
    guardar_captura(driver, "Foto4")
    time.sleep(5)
    #driver.execute_script("arguments[0].scrollIntoView();", link)

    time.sleep(5)
    assert "Build apps users love with AI-driven insights" in driver.page_source
    
    driver.quit()

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    textbox = driver.find_element(By.ID, "user-name")

    textbox.send_keys("standard_user")

    textbox = driver.find_element(By.ID, "password")

    textbox.send_keys("secret_sauce")

    time.sleep(10)

    button = driver.find_element(By.ID, "login-button")
    button.click()

    assert "Swag Labs" in driver.page_source