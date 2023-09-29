import sys
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (kata_assistant) to the system path
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from project.services.codewars_service import CodewarsService

def test_get_challenge_info():
    challenge_url = 'https://www.codewars.com/kata/520446778469526ec0000001/train/python'
    python_code = CodewarsService().get_challenge_info(challenge_url)
    assert python_code is not None
    assert isinstance(python_code, str)

