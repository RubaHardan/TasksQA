import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import sys
from Fucnctions import WebActions

@pytest.mark.usefixtures("driver_init")
class Test_chrome_firefox:
    def test_signup_with_positive_secnario(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[2]/a")


        wait = WebDriverWait(driver_init, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = driver_init.find_element(By.NAME, "login[password]")
        password_field.send_keys("hardanrubA1234")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()

        # Check if the user is redirected to the home page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/")
        assert "https://magento.softwaretestingboard.com/customer/account/" in driver_init.current_url




    def test_signup_with_negtive_secnario1_email_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[2]/a")


        wait = WebDriverWait(driver_init, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("rubahardan.com")

        password_field = driver_init.find_element(By.NAME, "login[password]")
        password_field.send_keys("hardanrubA1234")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()

        #Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
        assert "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/" in driver_init.current_url

    def test_signup_with_negtive_secnario2_password_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[2]/a")


        wait = WebDriverWait(driver_init, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = driver_init.find_element(By.NAME, "login[password]")
        password_field.send_keys("rrrrrrrggggg")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()

        # Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
        assert "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/" in driver_init.current_url


    def test_signup_with_negtive_secnario3_email_and_password_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[2]/a")


        wait = WebDriverWait(driver_init, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("rubahardan.com")

        password_field = driver_init.find_element(By.NAME, "login[password]")
        password_field.send_keys("rrrrrrrggggg")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()

        # Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
        assert "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/" in driver_init.current_url
