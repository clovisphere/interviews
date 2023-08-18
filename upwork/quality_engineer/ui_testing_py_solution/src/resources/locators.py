from selenium.webdriver.common.by import By


class GgLocators:
    """Google search page locators."""
    search_field = (By.NAME, 'q')
    result_container = (By.XPATH, '//div[@class="kvH3mc BToiNc UK95Uc"]')
    title = (By.XPATH, './/h3')
    link = (By.XPATH, './/div[@class="yuRUbf"]/a')
    description = (By.XPATH, './/div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]')


class DkLocators:
    """DuckDuckGo search engine locators."""
    search_field = (By.NAME, 'q')
    result_container = (By.XPATH, '//div[@class="nrn-react-div"]')
    title = (By.XPATH, './/h2')
    link = (By.XPATH, './/a')
    description = (By.XPATH, './/div[@class="OgdwYG6KE2qthn9XQWFC"]/span')
