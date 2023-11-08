import requests
import json
from seleniumwire import webdriver
from seleniumwire.utils import decode



class CodewarsService:
    def __init__(self, user='', page='0'):
        self.user = user
        self.page = page

    def get_challenge_info(self, challenge_url):
        try:
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options = options)
            driver.get(challenge_url)
            for request in driver.requests:
                if request.url.split('/')[-1] == 'session':
                    session = request
            response = session.response
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None

        if response is not None:
            body = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity')))
            url = f'https://www.codewars.com/api/v1/code-challenges/{challenge_url.split("/")[-3]}'

            challenge_info = requests.get(url).json()
            challenge_info['code'] = {'challenge_code': body['setup'], 'test_code': body['exampleFixture']}
            return challenge_info

        else:
            print(
                f"Error fetching challenge.")
            return None