import sqlite3


class DB:

    def __init__(self):
        self.conn = sqlite3.connect('Users', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def add_user(self, login, email, hashed_password):
        self.cursor.execute("INSERT INTO 'Users'(Name, Email, Password) VALUES(?, ?, ?)",
                            (login, email, hashed_password,))
        return self.conn.commit()

    def is_user_exist(self, email):
        result = self.cursor.execute("SELECT Name FROM Users WHERE Email = ?", (email,))
        return result.fetchone()

    def get_password(self, name):
        result = self.cursor.execute("SELECT Password FROM Users WHERE Name = ?", (name,))
        return result.fetchone()[0]


db = DB()
print(bool(db.is_user_exist('Cymaxim27@gmail.com')))
