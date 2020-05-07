import sqlite3

class Database:
    def __init__(self,db):
        self.db = sqlite3.connect(db)
        self.cur = self.db.cursor()
        self.db.commit()

    def create_table(self,table_name):
        self.cur.execute('CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREAMENT PRIMARY KEY, question VARCHAR(500)) '.format(table_name,))
        self.db.commit()

    def insert(self,table_name,question):
        self.cur.execute('INSERT INTO ? VALUES(NULL, ?)',(table_name,question))
        self.db.commit()

    def view(self,table_name):
        self.cur.execute('SELECT * FROM ?',(table_name,))
        row = self.cur.fetchall()
        return row

    def delete(self,table_name,id):
        self.cur.execute("DELETE FROM ? WHERE id = ?", (table_name,id))
        self.conn.commit()

    def show_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master where type='table'")
        row = self.cur.fetchall()
        return row

    def __del__(self):
        self.db.close()
    
