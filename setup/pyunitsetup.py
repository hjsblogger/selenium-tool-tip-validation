import sys
import os
from os import environ
from dotenv import load_dotenv
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *
from selenium import webdriver

from selenium.webdriver.remote.client_config import ClientConfig

load_dotenv(".env")
exec_platform = os.getenv('EXEC_PLATFORM')

class pyunit_setup:    
    def __init__(self):
        if exec_platform == 'cloud':
            username = environ.get('LT_USERNAME', None)
            access_key = environ.get('LT_ACCESS_KEY', None)

            ch_options = webdriver.ChromeOptions()

            lt_options = {}
            lt_options["build"] = "Build: Getting tooltip text for element validation in Selenium"
            lt_options["project"] = "Project: Getting tooltip text for element validation in Selenium"
            lt_options["name"] = "Test: Getting tooltip text for element validation in Selenium"

            lt_options["browserName"] = "Chrome"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "macOS Sonoma"

            lt_options["console"] = "error"
            lt_options["w3c"] = True
            lt_options["headless"] = False

            ch_options.set_capability('LT:Options', lt_options)

            gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

            # Create a secure ClientConfig
            # Reference - https://www.selenium.dev/documentation/webdriver/drivers/http_client/
            client_config = ClientConfig(
                remote_server_addr="@hub.lambdatest.com/wd/hub",
                keep_alive=True
            )
            self.driver = webdriver.Remote(
                command_executor = gridURL,
                options = ch_options,
                client_config=client_config
            )
        elif exec_platform == 'local':
            ch_options = ChromeOptions()

            # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
            # to trigger browser in headless mode

            # Enable headless mode for tests like web scraping, API testing, etc.    
            # ch_options.add_argument("--headless=new")
            self.driver = webdriver.Chrome(options=ch_options)
  
    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            self.driver.quit()