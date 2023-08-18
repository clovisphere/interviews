import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# use for both implicitly and explicitly wait
WAIT_TIME = 10


@pytest.fixture
def browser():
    """creates an instance of the browser"""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(WAIT_TIME)
    browser.get("http://127.0.0.1:3000")
    yield browser
    browser.quit()


class TestUI:

    # titles to use for the tests
    TITLES = [
        "Zoom call with John",
        "Buy some ice cream",
        "Walk the dog",
        "Code review",
        "Take Hailey to the swimming pool",
    ]

    TITLES_TO_MARK_AS_COMPLETED = [
        "Zoom call with John",
    ]

    TITLES_TO_DELETE = [
        "Buy some ice cream",
    ]

    @pytest.mark.parametrize("title", TITLES)
    def test_add_todo(self, browser, title):
        """
        Test that the user can add a todo
        """
        browser.find_element(By.CSS_SELECTOR, "input.input.form-control").send_keys(title)
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mb-3").submit()
        # get all span elements
        WebDriverWait(browser, WAIT_TIME).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span"))
        )
        span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
        assert title in span_texts

    @pytest.mark.parametrize("title", TITLES_TO_MARK_AS_COMPLETED)
    def test_mark_todo_as_completed(self, browser, title):
        """ Test that the user can mark a todo as completed """
        try:
            el = WebDriverWait(browser, WAIT_TIME).until(
                # make sure the title we want to 'mark as done' is visible
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{title}']"
                                                      f"//following-sibling::div//button[1]"))
            )
            el.click()  # click the 'mark as done/complete' button
            span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
            assert title in span_texts
        except TimeoutException:
            # todo: add an error message.. maybe:-)
            assert False

    @pytest.mark.parametrize("title", TITLES_TO_DELETE)
    def test_delete_todo(self, browser, title):
        """ Test that the user can delete a todo """
        try:
            el = WebDriverWait(browser, WAIT_TIME).until(
                # make sure the title we want to delete is visible
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{title}']"
                                                      f"//following-sibling::div//button[2]"))
            )
            el.click()  # click the delete button
            span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
            assert title not in span_texts
        except TimeoutException:
            # todo: add an error message.. maybe:-)
            assert False

    def test_title_cannot_be_longer_than_100_character(self, browser):
        """
        Test that the user cannot add a todo with a title longer than 100 characters
        """
        browser.find_element(By.CSS_SELECTOR, "input.input.form-control").send_keys(
            "a" * 101
        )
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mb-3").submit()
        # get all span elements
        WebDriverWait(browser, WAIT_TIME).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span"))
        )
        span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
        # NOTE: in a perfect world, the app/ui would display an error message
        assert "a" * 101 not in span_texts

    def test_title_cannot_be_empty(self, browser):
        """
        Test that the user cannot add a todo that doesn't have a title
        """
        browser.find_element(By.CSS_SELECTOR, "input.input.form-control").send_keys("")
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mb-3").submit()
        # get all span elements
        WebDriverWait(browser, WAIT_TIME).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span"))
        )
        span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
        # NOTE: in a perfect world, the app/ui would display an error message
        assert "" not in span_texts

    @pytest.mark.skip(reason="a better implementation is needed")
    @pytest.mark.parametrize("title", TITLES_TO_MARK_AS_COMPLETED)
    def test_task_marked_as_completed_cannot_be_deleted(self, browser, title):
        try:
            el = WebDriverWait(browser, WAIT_TIME).until(
                # make sure the title we want to delete is visible
                # we should check if it's marked as 'done/complete'
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{title}']"
                                                      f"//following-sibling::div//button[2]"))
                )
            el.click()  # click the delete button
            span_texts = [item.text for item in browser.find_elements(By.CSS_SELECTOR, "span")]
            assert title in span_texts
        except TimeoutException:
            # todo: add an error message.. maybe:-)
            assert False

    @pytest.mark.skip(reason="we currently can't edit a todo from the UI")
    def test_edit_todo(self, browser):
        pass
