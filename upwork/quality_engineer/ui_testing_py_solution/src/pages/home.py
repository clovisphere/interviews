from typing import Any, List, Dict
from src.pages.base import BasePage


class HomePage(BasePage):
    """home page action methods come here."""

    def search_keyword(self, keyword: str, locator: Any):
        """searches for the keyword passed in."""
        self.enter_text(locator.search_field, keyword)

    def get_results(self, locator: Any) -> List[Dict]:
        """gets the search result."""
        try:
            containers = self.driver.find_elements(*locator.result_container)
            for container in containers:
                title = container.find_element(*locator.title).text
                link = container.find_element(
                    *locator.link).get_attribute('href')
                description = container.find_element(
                    *locator.description).get_attribute('innerText')
                if title and link and description:
                    self.result.append({
                        'title': title,
                        'link': link,
                        'description': description
                    })
        except Exception as ex:  # too broad exception clause, not good:-(
            pass  # TODO: handle exception
        return self.result
