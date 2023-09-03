import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

ROOT = os.path.dirname(os.path.dirname(__file__))
WAIT_TIME = 10


@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    driver = webdriver.Chrome(os.path.join(ROOT, 'resources/chromedriver'))
    driver.implicitly_wait(WAIT_TIME)
    driver.get('https://the-internet.herokuapp.com/')
    yield driver
    driver.quit()


class TestBrowserAutomation:
    def test_print_text_in_each_frame(self, browser):
        try:
            browser.find_element_by_link_text('Frames').click()
            browser.find_element_by_link_text('Nested Frames').click()
            for inner_frame in ['frame-middle', 'frame-bottom', 'frame-left', 'frame-right']:
                if 'bottom' not in inner_frame:
                    outer_frame = WebDriverWait(browser, WAIT_TIME). \
                        until(EC.presence_of_element_located((By.NAME, 'frame-top')))
                    browser.switch_to.frame(outer_frame)
                    browser.switch_to.frame(inner_frame)
                else:
                    browser.switch_to.frame(inner_frame)
                text = browser.find_element_by_tag_name('body').text
                print(text)  # to print result, run py.test with -s option, e.g 'pytest -p no:cacheprovider -s'
                assert text in ['MIDDLE', 'RIGHT', 'BOTTOM', 'LEFT']
                browser.switch_to.default_content()  # go back to parent frame
        except (NoSuchElementException, NoSuchFrameException) as e:
            pytest.fail(f'an exception occurred - {e}')

    def test_read_and_print_text_after_page_has_been_loaded(self, browser):
        browser.get('http://the-internet.herokuapp.com/dynamic_loading/1')  # navigate to a new page
        browser.find_element_by_tag_name('button').click()
        greeting = WebDriverWait(browser, WAIT_TIME).until(EC.visibility_of_element_located((By.ID, 'finish')))
        print(greeting.text)  # to print result, run py.test with -s option, e.g 'pytest -p no:cacheprovider -s'
        assert greeting.text == 'Hello World!'

    def test_traverse_table_and_highlight_elements(self, browser):
        browser.get('https://the-internet.herokuapp.com/challenging_dom')
        trs = browser.find_elements(By.TAG_NAME, 'tr')  # all rows:-)

        # Highlight the text in the third row
        td3 = trs[3].find_elements(By.TAG_NAME, 'td')   # 3rd row
        TestBrowserAutomation.highlight_element(td3[5])

        # Highlight the delete link in the row containing “Apeirian7”
        td8 = trs[8].find_elements(By.TAG_NAME, 'td')
        TestBrowserAutomation.highlight_element(td8[6].find_element_by_link_text('delete'))

        # Highlight the edit link for the row containing “Apeirian2”
        TestBrowserAutomation.highlight_element(td3[6].find_element_by_link_text('edit'))

        # Highlight “Definiebas7” for two seconds, then highlight “Iuvaret7” for two seconds
        TestBrowserAutomation.highlight_element(td8[3])
        TestBrowserAutomation.highlight_element(td8[0])

        # Click the Green button
        browser.find_element_by_class_name('success').click()

    @classmethod
    def highlight_element(cls, element, effect_time=2, color='red', border=1):
        """Highlights (blinks) a Selenium Web-driver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)
