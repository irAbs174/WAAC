import sqlite3

class DB:
    # Define path to the database
    database_path = 'db.sqlite3'

    # Connect function
    def connect(self):
        try:
            con = sqlite3.connect(self.database_path)
            cur = con.cursor()
            return con, cur

        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None, None

    # Check if user exists
    def check_first_run(self):
        try:
            con, cur = self.connect()
            if con is None or cur is None:
                return None

            res = cur.execute("SELECT name FROM user").fetchone()
            con.close()
            return res

        except sqlite3.OperationalError as e:
            print(f"Operational error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # Create user table and add first user
    def create_user_table(self, name, phone):
        try:
            con, cur = self.connect()
            if con is None or cur is None:
                return None

            cur.execute("""
                CREATE TABLE IF NOT EXISTS user(
                    name TEXT,
                    phone TEXT,
                    token TEXT
                )
            """)
            
            cur.execute("INSERT INTO user (name, phone, token) VALUES (?, ?, '')", (name, phone))
            con.commit()  # Commit the transaction
            con.close()

        except sqlite3.OperationalError as e:
            print(f"Operational error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Create an instance of the DB class
db_instance = DB()

# Now you can call methods on this instance
con, cur = db_instance.connect()  # This will connect to the database
