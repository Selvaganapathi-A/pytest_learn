import requests


def get_todo(url:str) -> requests.Response:
    response = requests.get(url)
    return response
