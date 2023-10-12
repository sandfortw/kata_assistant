import requests
# from urllib.parse import quote
# from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, WebDriverException
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json



class CodewarsService:
    def __init__(self, user='', page='0'):
        self.user = user
        self.page = page

    def get_challenge_info(self, challenge_url):
        """
        Uses chrome webdriver and beautiful soup to parse html and return code.
        """
        try:
            driver = webdriver.Chrome()
            # driver.implicitly_wait(5)
            driver.get(challenge_url)
            session = ''
            for request in driver.requests:
                if request.url.split('/')[-1] == 'session':
                    session = request
            response = session.response
            # body = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity')))
            # import ipdb; ipdb.set_trace()
            # response = driver.page_source
        except (TimeoutException, WebDriverException) as e:
            print(f"An error occurred: {e}")
            response = None

        if response is not None:
            body = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity')))
            # soup = BeautifulSoup(response, 'html.parser')
            # import ipdb; ipdb.set_trace()
            # code_elements = soup.find_all('div', class_='CodeMirror-code')
            # # code_elements = soup.find_all('pre', class_='CodeMirror-line')
            # challenge_elements = code_elements[0].find_all('pre', class_='CodeMirror-line')
            # challenge_code = "\n".join(element.text
            #                         for element in challenge_elements)
            # test_elements = code_elements[1].find_all('pre', class_='CodeMirror-line')
            # test_code = "\n".join(element.text
            #                         for element in test_elements)
            # code_elements = soup.find_all('pre', class_='CodeMirror-line')
            # import ipdb; ipdb.set_trace()
            # python_code = "\n".join(element.text.strip()
            #                         for element in code_elements)
            url = f'https://www.codewars.com/api/v1/code-challenges/{challenge_url.split("/")[-3]}'

            challenge_info = requests.get(url).json()
            challenge_info['code'] = {'challenge_code': body['setup'], 'test_code': body['exampleFixture']}
            return challenge_info

        else:
            print(
                f"Error fetching challenge.")
            return None
        
    #Comment the following back in, if this feature ever gets implemented:
    # def get_completed_challenges(self):
    #     """Retrieve completed challenges from CodeWars API. Returns an object."""
    #     url = f'http://www.codewars.com/api/v1/users/{quote(self.user)}/code-challenges/completed?page={self.page}'

    #     response = requests.get(url)

    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         raise Exception(
    #             f"Error fetching challenge. Status code: {response.status_code}")