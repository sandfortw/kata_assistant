import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

class CodewarsService:
    def __init__(self, user='Weston Sandfort', page='0'):
        self.user = user
        self.page = page

    def get_completed_challenges(self):
        """Retrieve completed challenges from CodeWars API."""
        url = f'http://www.codewars.com/api/v1/users/{quote(self.user)}/code-challenges/completed?page={self.page}'
        
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching challenge. Status code: {response.status_code}")
    
    # def get_challenge_data(challenge_id):
    #     """Retrieve data from a challenge id"""
    #     # 5202ef17a402dd033c000009

    def get_challenge_info(challenge_url):
    # Make an HTTP request to the challenge URL
        response = requests.get(challenge_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            import ipdb; ipdb.set_trace()
            # Find all elements with class starting with 'cm-'
            code_elements = soup.find_all(class_=lambda x: x and x.startswith('cm-'))
            
            # Extract the text content from these elements
            python_code = "\n".join(element.text.strip() for element in code_elements)

            return python_code.strip()

        else:
            print(f"Error fetching challenge. Status code: {response.status_code}")
            return None
        
    # Example usage
    challenge_url = 'https://www.codewars.com/kata/valid-braces/train/python'
    python_code = get_challenge_info(challenge_url)

    if python_code:
        print("Python Code:")
        print(python_code)