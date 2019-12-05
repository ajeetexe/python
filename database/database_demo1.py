import mysql.connector
import time


class Demo1:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost', user='root', passwd='ajeet')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE DATABASE IF NOT EXISTS demo_py')
        self.conn.commit()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS demo_py.demo_table(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(10), "
            "address VARCHAR(10))")
        self.conn.commit()

    def insert(self, name, address):
        self.cur.execute(
            "INSERT INTO demo_py.demo_table VALUES(NULL, %s, %s)", (name, address))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM demo_py.demo_table")
        row = self.cur.fetchall()
        return row

    def update(self, id, name, address):
        self.cur.execute(
            "UPDATE demo_py.demo_table SET name = %s, address = %s where id = %s", (name, address, id))
        self.conn.commit()

    def search(self, name="", address=""):
        self.cur.execute(
            "SELECT * FROM demo_py.demo_table where name = %s or address = %s", (name, address))
        row = self.cur.fetchall()
        return row

    def delete(self, id):
        self.cur.execute("DELETE FROM demo_py.demo_table WHERE id = %s", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def user_input(self):
        while True:
            print('1->Create Table\n2->Drop Table\n3->Insert Data\n4->Delete Data\n5->Update '
                  'Data\n6->Search\n7->View\n0->Exit')
            choice = int(input('Enter Your Option'))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                name = input('Enter Name')
                address = input('Enter address')
                database.insert(name, address)
            elif choice == 4:
                mid = input('Enter Id')
                if database.view() == mid:
                    database.delete(mid)
                    print('Data deleted Successfully')
                    time.sleep(2)
                else:
                    print('This id not found')
                    time.sleep(2)
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                for x in database.view():
                    print(x[0], x[1], x[2])
                time.sleep(5)
            elif choice == 0:
                break


if __name__ == '__main__':
    database = Demo1()
    # database.user_input()
    for x in database.view():
        print(x[0], x[1], x[2])
