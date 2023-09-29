from project.services.codewars_service import CodewarsService

def test_get_challenge_info():
    challenge_url = 'https://www.codewars.com/kata/520446778469526ec0000001/train/python'
    python_code = CodewarsService().get_challenge_info(challenge_url)
    assert python_code is not None
    assert isinstance(python_code, str)


