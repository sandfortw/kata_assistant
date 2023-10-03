from project.services.codewars_service import CodewarsService
from random import choice


def test_get_challenge_info():
    """
    Proves that getting challenge info returns a string, and that it contains at least the substring 'def'.
    """
    challenge_url = 'https://www.codewars.com/kata/520446778469526ec0000001/train/python'
    python_code = CodewarsService().get_challenge_info(challenge_url)['code']
    assert python_code is not None
    assert isinstance(python_code, str)
    assert 'def' in python_code


def test_get_completed_challenges():
    """
    Proves that get_completed_challenges returns an object with challenge data.
    """
    json = CodewarsService(
        user='Weston Sandfort',
        page='0').get_completed_challenges()
    assert json is not None
    assert isinstance(json, dict)
    assert isinstance(json['data'], list)
    assert isinstance(choice(json['data']), dict)
    assert isinstance(choice(json['data'])['name'], str)
    assert isinstance(choice(json['data'])['id'], str)
