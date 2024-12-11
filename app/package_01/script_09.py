class RegisteredUser:

    def __init__(self) -> None:
        self.__users__: list[str] = list()

    def register(self, user: str):
        self.__users__.append(user)
        return len(self.__users__)

    def check_user(self, user: str):
        return user in self.__users__

    def unregister(self, user: str):
        if not self.check_user(user):
            raise ValueError('User not registered.', user)
        self.__users__.remove(user)
        return len(self.__users__)
