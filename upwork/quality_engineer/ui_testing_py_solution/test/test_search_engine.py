import os
import unittest
from parameterized import parameterized
from test.test_base import BaseTest
from src.pages.home import HomePage
from src.resources.locators import GgLocators, DkLocators


class SearchEngineTest(BaseTest):
    """Test case for searching keyword using google search & bing."""

    CUMULATIVE_SEARCH_RESULT = []  # keep track of result of the 1st search engine

    @parameterized.expand([
        ('Google', 'https://google.com', GgLocators),
        ('DuckDuckGo', 'https://duckduckgo.com/', DkLocators),
    ])
    def test_search_keyword_using_either_google_or_bing(self, engine, url, locator):
        """searches for the keyword using google."""
        print(f'3. go to {url}', end=' ')
        home_page = HomePage(self.driver, url)
        print('✅')
        # page title should be <Google> or <Bing>
        self.assertIn(engine, home_page.get_title(
            engine), 'page title don\'t match')
        print('4. search for the keyword using google', end=' ')
        home_page.search_keyword(os.environ.get('KEYWORD'), locator)
        print('✅')
        # the search result page should have the <KEYWORD> in its title, e.g "python - Google Search"
        self.assertIn(os.environ.get('KEYWORD'), home_page.get_title(os.environ.get('KEYWORD')),
                      'keyword not found in title')
        print('5. get the search result', end=' ')
        search_result = home_page.get_results(locator)
        print(f'{"✅" if len(search_result) > 0 else "❌"}')
        if search_result:
            print(f"6. <{os.environ.get('KEYWORD')}> found in at least one of attribute of "
                  f"each item from parsed search results", end=' ')
            for result in search_result:
                if os.environ.get('KEYWORD').lower() in result['title'].lower() or \
                        os.environ.get('KEYWORD').lower() in result['link'].lower() or \
                        os.environ.get('KEYWORD').lower() in result['description'].lower():
                    self.assertTrue(True)
                    print('✅', end=' ')
                else:
                    print(f'❌', end=' ')
            print('\n7. print the search result')
            self.pretty_print(search_result)
            self.compare_search_results(search_result)
        else:
            # if no search result found, then we should fail the test
            self.assertTrue(search_result, 'no search result found')

    def compare_search_results(self, engine_search_result):
        """display commonalities between the two search engines results"""
        common_search_result = []
        if not SearchEngineTest.CUMULATIVE_SEARCH_RESULT:
            SearchEngineTest.CUMULATIVE_SEARCH_RESULT.append(
                engine_search_result)
        else:
            for result in engine_search_result:
                if result['link'] in SearchEngineTest.CUMULATIVE_SEARCH_RESULT[0]:
                    common_search_result.append(result)
            print(
                f"\n{'no common (search) result found' if not common_search_result else common_search_result=}")


if __name__ == '__main__':
    unittest.main()
