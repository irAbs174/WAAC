import sqlite3
import secrets

class DBUser:
    def connect(self):
        try:
            con = sqlite3.connect('db.sqlite3')
            cur = con.cursor()
            return con, cur
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None, None

    def check_user_table(self):
        con, cur = self.connect()
        try:
            res = cur.execute("""
                SELECT name FROM user;
            """).fetchall()
        except:
            res = cur.executescript("""
                BEGIN;
                CREATE TABLE user(name, phone, token);
                COMMIT;
            """)
        finally:
            con.close()
            return res

    def auth(self, name, phone):
        con, cur = self.connect()
        q = cur.execute("""SELECT name FROM user WHERE name=? AND phone = ?""", (name, phone)).fetchall()
        if q == []:
            res = {'NOT ALLOWED'}
        else:
            token = secrets.token_hex(32)
            res = cur.execute("""
                UPDATE user SET token=? WHERE name=? and phone=?;
            """,(token, name, phone)).fetchall()
            con.commit()
            con.close()
        return res

    def register(self, name, phone):
        con, cur = self.connect()
        q = cur.execute("""SELECT name FROM user WHERE name = ? AND phone = ?""", (name, phone)).fetchall()
        if q == []:
            res = cur.execute("""INSERT INTO user(name, phone) VALUES (?, ?)""", (name, phone))
        else:
            res = {'USER ALREDY EXISTS! '}

        con.commit()
        con.close()
        return res
