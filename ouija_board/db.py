"""This module contains database operations for creating, inserting, and
retrieving the phrase to be displayed"""

import sqlite3


class DBOperations:
    """This class contains methods to create and manipulate a database"""

    def __init__(self, db_file):
        """On instantiation, this class will create a db connection
        attribute

        :param db_file: Name of the database to initialize
        """

        self.db_file = db_file

        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)
        except sqlite3.Error as error:
            print(error)

    def create(self):
        """This method creates the table if it doesnt exist"""

        sql = """CREATE TABLE IF NOT EXISTS phrase(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME,
        remote_ip STRING,
        phrase STRING)"""

        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def insert(self, timestamp, remote, phrase):
        """This method inserts data into the database

        :param timestamp: datetime of the insert from client
        :param remote: IP address of who submitted the phrase
        :param phrase: Phrase to be displayed
        :return: The last ROWID of the DB
        """

        sql = """INSERT INTO phrase (timestamp, remote_ip, phrase) VALUES (?, ?, ?)"""

        cur = self.conn.cursor()
        cur.execute(sql, [timestamp, remote, phrase])
        self.conn.commit()

        return f"Last ROWID: {cur.lastrowid}"

    def retrieve(self):
        """This method retrieves the last phrase submitted from the database"""

        cur = self.conn.cursor()
        cur.execute("SELECT phrase FROM phrase ORDER BY phrase.id DESC LIMIT 1")

        phrase = cur.fetchall()

        try:
            return phrase[0][0]
        except IndexError:
            return "INIT"
