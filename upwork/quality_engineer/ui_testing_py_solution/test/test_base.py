import os
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from prettytable import PrettyTable, MARKDOWN


class BaseTest(unittest.TestCase):
    """Base class for all tests."""

    def setUp(self) -> None:
        """called before any test is run."""
        browser = os.environ.get('BROWSER').lower()
        if browser in ['firefox', 'chrome']:
            self.driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()), options=self.add_options_to_browser()) \
                if browser == 'firefox' else webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=self.add_options_to_browser())
            print(f'\n1. start {browser} browser ✅')
            # we need to clear cookies
            print('2. clear cookies ✅')
            self.driver.delete_all_cookies()
        else:
            print(f"{'no browser specified' if browser else 'browser not supported'}\nexiting...")
            sys.exit(1)

    def pretty_print(self, search_result):
        """pretty prints the search result."""
        table = PrettyTable(['Title', 'Link', 'Short Description'])
        for row in search_result:
            table.add_row([row['title'], row['link'], row['description']])
        table.max_table_width = 150
        table.align = 'l'
        print(table.get_string(sortby='Title', format=MARKDOWN))

    def add_options_to_browser(self):
        """adds options to the driver."""
        options = webdriver.ChromeOptions() if os.environ.get('BROWSER') == 'chrome' \
            else webdriver.FirefoxOptions()
        options.add_argument('--lang=en-GB')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return options

    def tearDown(self) -> None:
        """called at the end of every test to clear resources"""
        self.driver.quit()
