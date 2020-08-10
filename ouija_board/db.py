import sqlite3


class DBFunctions:
    def __init__(self, db_file):
        self.db_file = db_file

        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)
        except sqlite3.Error as e:
            print(e)

    def update(self, phrase):

        sql = f'''UPDATE phrase SET phrase = ?'''

        cur = self.conn.cursor()
        cur.execute(sql, [phrase])
        self.conn.commit()

        return f"SQLite Status: {cur.lastrowid}"

    def retrieve(self):

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM phrase")

        phrase = cur.fetchall()

        return phrase[0][0]
