from UsersDBAPI import *

class UserData:
    _username: str
    _user_id: int

    # register user and return true if user with same data already exists
    def register(self, username: str, user_id: int) -> bool: # TODO: add pin-code
        self._username = username
        self._user_id = user_id

        if UsersDBAPI.is_exists(self._user_id):
            return True

        self._save_to_sql()
        return False

    def login(self, user_id: int):
        self._get_from_sql(user_id)

    def _save_to_sql(self):
        UsersDBAPI.save_to_db(self._user_id, self._username, None)

    def _try_get_from_sql(self):
        UsersDBAPI.get_from_sql(self._user_id)