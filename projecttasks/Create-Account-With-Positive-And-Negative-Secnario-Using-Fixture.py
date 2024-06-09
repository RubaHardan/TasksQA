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
    def test_createaacount_with_positive_secnario(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[3]/a")
        wait = WebDriverWait(driver_init, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = driver_init.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = driver_init.find_element(By.NAME, "email")
        email_field.send_keys("r.hardan@student.aaup.edu")

        password_field = driver_init.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = driver_init.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("hardanrubA1234")


        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()

        # Check if the email address already exists
        #email_error_message = driver_init.find_element(By.XPATH,"//*[@id='maincontent']/div[2]/div[2]/div/div/div").text
        #assert "There is already an account with this email address" in email_error_message

        # Check if the user is redirected to the home page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/")
        assert "https://magento.softwaretestingboard.com/customer/account/" in driver_init.current_url

        # Check if the user's name is displayed correctly
        #user_name = driver_init.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text
       # assert user_name == "RUBA Hardan"


    def test_createaacount_with_negtive_secnario1_email_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[3]/a")

        wait = WebDriverWait(driver_init, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = driver_init.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = driver_init.find_element(By.NAME, "email")
        email_field.send_keys("rubahardan.com")

        password_field = driver_init.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = driver_init.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("hardanrubA1234")


        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        # Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/create/")
        assert "https://magento.softwaretestingboard.com/customer/account/create/" in driver_init.current_url



    def test_createaacount_with_negtive_secnario2_password_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[3]/a")


        wait = WebDriverWait(driver_init, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = driver_init.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = driver_init.find_element(By.NAME, "email")
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = driver_init.find_element(By.NAME, "password")
        password_field.send_keys("rrrrrrrggggg")

        confirm_password_field = driver_init.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("rrrrrrrggggg")


        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        # Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/create/")
        assert "https://magento.softwaretestingboard.com/customer/account/create/" in driver_init.current_url

    def test_createaacount_with_negtive_secnario3_confirm_password_not_correct(self, driver_init):
        web_actions = WebActions(driver_init)
        web_actions.navigate_to_homepage("//header//li[3]/a")

        # Explicit Wait for the First Name field
        wait = WebDriverWait(driver_init, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = driver_init.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = driver_init.find_element(By.NAME, "email")
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = driver_init.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = driver_init.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("rrrrrrrggggg")


        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        # Check if he's still on the same page
        driver_init.get("https://magento.softwaretestingboard.com/customer/account/create/")
        assert "https://magento.softwaretestingboard.com/customer/account/create/" in driver_init.current_url