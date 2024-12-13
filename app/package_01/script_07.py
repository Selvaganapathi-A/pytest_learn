USER: dict[str, str] = {
    'name': "Tesla",
    'access-code': '200',
}


def grant_user_access(name: str):
    if name != USER['name']:
        USER['access-status'] = 'Access Denied'
        USER['access-code'] = '404'
        return False
    USER['access-status'] = 'Access Granted'
    USER['service'] = 'aws'
    #
    return True
