import os
from os import environ
import time
import sys
import warnings

import unittest
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

sys.path.append(sys.path[0] + "/../..")
from setup.pyunitsetup import pyunit_setup

time_sleep = 2

########################## Locators #########################
xSubmitForm = "//a[.='Input Form Submit']"
xInpName = "//input[@id='name']"
cInpName = "#name"
xInpEmail = "//form[@id='seleniumform']//input[@name='email']"
xInpPassword = "//input[@name='password']"
cssCompany = "#company"
cWebName = "#websitename"
xInpCountry = "//select[@name='country']"
xInpCity = "//input[@id='inputCity']"
cssAddress1 = "[placeholder='Address 1']"
cssAddress2 = "[placeholder='Address 2']"
cssInpState = "#inputState"
cssInpZip = "#inputZip"
cssInpButton = ".bg-lambda-900"
nameSearchBox = "search"

# Suppress the specific warning
warnings.filterwarnings("ignore", category=UserWarning,
    message=".*Embedding username and password in URL.*")

load_dotenv(".env")
exec_platform = os.getenv('EXEC_PLATFORM')

setting = pyunit_setup()

class TestFormInput(unittest.TestCase):
    def test_get_tooltip_text(self):
        resultant_str = "Thanks for contacting us, we will get back to you shortly."

        setting.setUp()
        driver = setting.driver

        driver.get("https://www.lambdatest.com/selenium-playground/")

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        try:
            element = driver.find_element(By.XPATH, xSubmitForm)
            element.click()

            elem_name = driver.find_element(By.XPATH, xInpName)
            elem_name.send_keys("Testing")
            time.sleep(time_sleep)

            elem_email = driver.find_element(By.XPATH, xInpEmail)
            # Enter email address without the @ sign
            elem_email.send_keys("testing")
            time.sleep(time_sleep)

            elem_pass = driver.find_element(By.XPATH, xInpPassword)
            elem_pass.send_keys("password")
            time.sleep(time_sleep)

            elem_comp = driver.find_element(By.CSS_SELECTOR, cssCompany)
            elem_comp.send_keys("LambdaTest")

            elem = driver.find_element(By.CSS_SELECTOR, cWebName)
            elem.send_keys("https://wwww.lambdatest.com")

            country_dropdown = Select(driver.find_element(By.XPATH, xInpCountry))
            country_dropdown.select_by_visible_text("United States")
            time.sleep(time_sleep)

            elem = driver.find_element(By.XPATH, xInpCity)
            elem.send_keys("San Jose")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssAddress1)
            elem.send_keys("Googleplex, 1600 Amphitheatre Pkwy")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssAddress2)
            elem.send_keys("Mountain View, CA 94043")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssInpState)
            elem.send_keys("California")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssInpZip)
            elem.send_keys("94088")
            time.sleep(time_sleep)

            # Click on the Submit button
            submit_button = driver.find_element(By.CSS_SELECTOR, cssInpButton)
            submit_button.click()
            time.sleep(2)

            # Get the tooltip text/validation message
            str_validation_mess = driver.execute_script(
                "return document.getElementById('inputEmail4').validationMessage;"
            )

            print("Validation Message:", str_validation_mess)

            # You need not use executeScript in Java since it can 
            # be done using "getAttribute(validationMessage)"
            # document.getElementById("input-email").validationMessage
            # However, getAttribute will not work with Selenium 4.27.0
            # https://github.com/SeleniumHQ/selenium/issues/13334

            # This will raise an assert and test will be failed
            # However our usecase is to capture the tool-tip text
            try:
                element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".success-msg"))
                )
                assert resultant_str in element.text, f"'{resultant_str}' not found in the specified element."
                if exec_platform == 'cloud':
                    driver.execute_script("lambda-status=failed")
            except Exception as e:
                if exec_platform == 'cloud':
                    driver.execute_script("lambda-status=failed")
                self.fail(f"Text '{resultant_str}' not found: {str(e)}")
            
            time.sleep(2)
        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Input Form Demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")

        if exec_platform == 'cloud':
            driver.execute_script("lambda-status=passed")
        print(f"Tool tip verification test passed")

    def tearDown(self):
        setting.tearDown()

if __name__ == "__main__":
    unittest.main()

# import os
# import sys

# # project_dir = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))
# sys.path.append(sys.path[0] + "/../..")
# # sys.path.append(project_dir)

# from setup.pyunitsetup import pyunit_setup


# try:
#     print("Current Working Directory:", os.getcwd())
#     # from setup.pyunitsetup import pyunit_setup
#     print("Import successful!")
# except ModuleNotFoundError as e:
#     print("Error:", e)
