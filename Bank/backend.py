import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS bank(id INTEGER PRIMARY KEY,name TEXT,balance REAL,account_no INTEGER, ' \
              'address TEXT) '
        self.curr.execute(sql)
        self.conn.commit()

    def insert(self, name, balance, account_no, address):
        self.curr.execute('INSERT INTO bank VALUES(NULL,?,?,?,?)', (name, balance, account_no, address))
        self.conn.commit()

    def search(self, name="", balance="", account_no="", address=""):
        self.curr.execute('SELECT * FROM bank WHERE name=? OR balance=? OR account_no=? OR address=?',
                          (name, balance, account_no, address))
        rows = self.curr.fetchall()
        return rows

    def view(self):
        self.curr.execute("SELECT * FROM bank")
        rows = self.curr.fetchall()
        return rows

    def delete(self, id):
        self.curr.execute("DELETE FROM bank WHERE Id=?", (id,))
        self.conn.commit()

    def update(self, id, name, balance, account_no, address):
        self.curr.execute("UPDATE bank SET name=?, balance=?, account_no=? ,address=? WHERE id=?",
                          (name, balance, account_no, address, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

