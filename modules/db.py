import sqlite3

# BASIC SQL TABLE MANAGER BY ET43 FOR IP SAVER API

"""
    Table Class:
        Create table - [name] [values]
        Check if table exists - [name] [values]
        Delete Table - [name]
        Add items to table - [name] [values]
        Get items from table - [name]

                 
"""

class table():
    def __init__(self):
        self.useless = 0
    
    def create(self, name):
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE {name}(
        ip STRING
        )
        """)
        conn.commit()
        cursor.close()
        return "Table Created!"
    
    def add(self, name, ip):
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        ex = cursor.execute(f"""INSERT INTO {name} (ip)
        VALUES ({ip})
        """)
        conn.commit()
        cursor.close()
        return "Succesfully Entered Values!"
    
    def get(self, name):
        query = f"""select * from {name}"""
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchall()

        for i in record:
            return f"""{str(i[0])}"""

    def validate(self, name):
        try:
            conn = sqlite3.connect("db.db")
            curr = conn.cursor()
            query = f'''select * from {name}'''  
            curr.execute(query)
            return True
        except sqlite3.OperationalError:
            return False
    
    def delete(self, name):
        conn = sqlite3.connect("db.db")
        curr = conn.cursor()
        query = f'''DROP TABLE {name}'''  
        curr.execute(query)
        return "Deleted!"
        

    


    