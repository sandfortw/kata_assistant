import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException


class CodewarsService:
    def __init__(self, user='', page='0'):
        self.user = user
        self.page = page

    def get_completed_challenges(self):
        """Retrieve completed challenges from CodeWars API. Returns an object."""
        url = f'http://www.codewars.com/api/v1/users/{quote(self.user)}/code-challenges/completed?page={self.page}'

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Error fetching challenge. Status code: {response.status_code}")

    def get_challenge_info(self, challenge_url):
        """
        Uses chrome webdriver and beautiful soup to parse html and return code.
        """
        try:
            driver = webdriver.Chrome()
            driver.get(challenge_url)
            response = driver.page_source
        except (TimeoutException, WebDriverException) as e:
            print(f"An error occurred: {e}")
            response = None

        if response is not None:
            soup = BeautifulSoup(response, 'html.parser')
            code_elements = soup.find_all('div', class_='CodeMirror-code')

            python_code = "\n".join(element.text.strip()
                                    for element in code_elements)
            url = f'https://www.codewars.com/api/v1/code-challenges/{challenge_url.split("/")[-3]}'

            challenge_info = requests.get(url).json()
            challenge_info['code'] = python_code.strip()
            return challenge_info

        else:
            print(
                f"Error fetching challenge. Status code: {response.status_code}")
            return None

CodewarsService().get_challenge_info("https://www.codewars.com/kata/520446778469526ec0000001/train/python")