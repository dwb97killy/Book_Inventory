import sqlite3

class Account():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, account TEXT, password TEXT)")
        self.conn.commit()

    def insert_table(self, account, password):
        self.cur.execute("INSERT INTO account VALUES (NULL, ?, ?)", (account, password))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM account")
        rows = self.cur.fetchall()
        return rows  # row的返回形式为list

    def search(self, account='', password=''):
        self.cur.execute("SELECT * FROM account WHERE account = ? AND password = ?", (account, password))
        rows = self.cur.fetchall()
        return rows  # row的返回形式为list

    def delete(self, id):
        self.cur.execute("DELETE FROM account WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, account='', password=''):
        self.cur.execute("UPDATE account SET account = ?, password = ? WHERE id = ?", (account, password, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

'''account = Account("account.db")
print(account.view())
#account.insert_table('123', '123')
print(account.search('123', 123))'''