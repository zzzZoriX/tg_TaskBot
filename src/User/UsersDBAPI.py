import sqlite3

class UsersDBAPI:
    """
    таблица имеет поля:
    user_id: integer not null - хранит тг-id пользователя
    username: text not null - хранит ник пользователя
    pin-code: text not null - (опционально) хранит пин-код от аккаунта пользователя
    """

    db_name: str = "Users"
    cursor: sqlite3.Cursor
    connection: sqlite3.Connection


    @staticmethod
    def init_db() -> None:
        UsersDBAPI.connection = sqlite3.connect(UsersDBAPI.db_name + ".db")
        UsersDBAPI.cursor = UsersDBAPI.connection.cursor()

    @staticmethod
    def create_db() -> None:
        create_db_sql = f"""
        CREATE TABLE IF NOT EXISTS {UsersDBAPI.db_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            pin_code TEXT NOT NULL
        )
        """

        UsersDBAPI.cursor.execute(create_db_sql)
        UsersDBAPI.connection.commit()

    @staticmethod
    def save_to_db(user_id: int = -1, username: str = "", pin_code: "str|None" = None) -> None:
        insert_into_db_sql = f"""
        INSERT INTO {UsersDBAPI.db_name}(user_id, username, pin_code)
        VALUES ({user_id}, {username}, {"NULL" if pin_code is None else pin_code})
        """

        UsersDBAPI.cursor.execute(insert_into_db_sql)
        UsersDBAPI.connection.commit()

    @staticmethod
    def get_from_sql(user_id: int):
        get_from_sql = f"""
        SELECT * FROM {UsersDBAPI.db_name} WHERE user_id = {user_id}
        """

        UsersDBAPI.cursor.execute(get_from_sql)
        getted_info = UsersDBAPI.cursor.fetchone()

        if getted_info is None:
            return None

        return getted_info[0]

    @staticmethod
    def is_exists(user_id: int) -> bool:
        is_exists_sql = f"""
        SELECT * FROM {UsersDBAPI.db_name} WHERE user_id = {user_id}
        """

        UsersDBAPI.cursor.execute(is_exists_sql)

        return UsersDBAPI.cursor.fetchone() is None