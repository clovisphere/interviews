import os
from typing import Any, Tuple
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """BasePage holds common functionality across the website."""

    def __int__(self, driver: Any, url: str) -> None:
        """called every time a new object is created."""
        self.driver = driver
        # navigate to the page
        self.driver.get(url)
        self.result = []

    def enter_text(self, by_locator: Tuple[str, str], text: str):
        """enters the text into the web element whose locator is passed in."""
        WebDriverWait(self.driver, float(os.environ.get('IMPLICIT_WAIT_TIME')))\
            .until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        self.driver.find_element(*by_locator).send_keys(Keys.RETURN)

    def get_title(self, title: str) -> str:
        """gets the title of the current web page."""
        WebDriverWait(self.driver, float(os.environ.get('IMPLICIT_WAIT_TIME')))\
            .until(EC.title_contains(title))
        return self.driver.title
