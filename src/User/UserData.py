class UserData:
    _username: str
    _user_id: int

    # register user and return true if user with same data already exists
    def register(self, username: str, user_id: int) -> bool: # TODO: add pin-code
        self._username = username
        self._user_id = user_id

        if self._check_is_exists():
            return True

        self._save_to_sql()

    def login(self, user_id: int):
        self._get_from_sql(user_id)

    def _save_to_sql(self):
        pass

    def try_get_from_sql(self, user_id: int):
        pass