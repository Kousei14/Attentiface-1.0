import sqlite3
from tkinter import messagebox

class Queries:
    def __init__(self):
        pass

    def read(self, database, table):
        conn = sqlite3.connect(database)

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()

        return data
    
    def read_v2(self, database, table, columns, 
                row_specific: bool = False, column_key: str = None, id: int = None):
        conn = sqlite3.connect(database)

        columns_str = ", ".join(columns)
        cursor = conn.cursor()

        if row_specific:
            cursor.execute(f"SELECT {columns_str} FROM {table} WHERE {column_key} = {int(id)}")
            data = cursor.fetchall()
        else:
            cursor.execute(f"SELECT {columns_str} FROM {table}")
            data = cursor.fetchall()
        return data

    def create(self, database, table, columns):
        if database is None:
            raise ValueError("Database name cannot be None")

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        with conn:
            if isinstance(columns, list):
                columns = ", ".join(columns)
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns})")
            conn.commit()
        
    def insert(self, database, table, columns, values, root=False):
        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            columns_str = ", ".join(columns)
            values_str = ", ".join(["?" for _ in columns])

            sql_insert = f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"

            cursor.execute(sql_insert, values)
            conn.commit()

            if root:
                messagebox.showinfo(
                    "Input Validation", 
                    "Input added successfully", 
                    parent = root
                )
        except Exception as es:
            if root:
                messagebox.showerror(
                    "Error Prompt", 
                    f"Error: {str(es)}", 
                    parent = root
                )
        finally:
            conn.close()

    def update(self, database, table, columns, values, on_key, root=False):
        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            set_clause = ", ".join([f"{col} = ?" for col in columns])
            sql_update = f"UPDATE {table} SET {set_clause} WHERE ID = {on_key}"

            cursor.execute(sql_update, values)
            conn.commit()

            if root:
                messagebox.showinfo(
                    "Input Validation", 
                    "Updated successfully", 
                    parent = root
                )
        except Exception as es:
            if root:
                messagebox.showerror(
                    "Error Prompt", 
                    f"Error: {str(es)}", 
                    parent = root
                )
        finally:
            conn.close()

    def delete(self, database, table, on_key, root=False):
        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]

            if count == 1:
                cursor.execute(f"DELETE FROM {table}")
                cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{table}'")
                conn.commit()

                if root:
                    messagebox.showinfo(
                        "Attentiface V 1.0",
                        "Data deleted successfully",
                        parent = root
                    )
            else:
                sql_delete = f"DELETE FROM {table} WHERE ID = {on_key}"
                cursor.execute(sql_delete)
                conn.commit()

                if root:
                    messagebox.showinfo(
                        "Attentiface V 1.0",
                        "Data deleted successfully",
                        parent = root
                    )
        except Exception as es:
            if root:
                messagebox.showerror(
                    "Attentiface V 1.0",
                    f"Error: {str(es)}",
                    parent = root
                )
        finally:
            conn.close()

    def delete_all(self, database, table, root=False):
        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM {table}")
            cursor.execute(f"DELETE FROM sqlite_sequence where name = '{table}'")

            conn.commit()
        except Exception as es:
            if root:
                messagebox.showerror(
                    "Attentiface V 1.0",
                    f"Error: {str(es)}",
                    parent = root
                )
        finally:
            conn.close()

    def search(self, database, table, search_key, search_string, root=False):
        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            if search_key == " Employee ID":
                word = "employee_id"
            elif search_key == " Last Name":
                word = "last_name"
            elif search_key == " First Name":
                word = "first_name"

            sql_search = f"SELECT * FROM {table} WHERE {word} LIKE '%{str(search_string)}%'"

            cursor.execute(sql_search)
            conn.commit()

            data = cursor.fetchall()

            return data
        except Exception as es:
            if root:
                messagebox.showerror(
                    "Attentiface V 1.0",
                    f"Error: {str(es)}",
                    parent = root
                )
        finally:
            conn.close()

    def print_all_values(self, database, table):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * from {table}")
        data = cursor.fetchall()

        return data
    
    def print_all_tables(self, database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        tables = cursor.fetchall()
        
        print(f"Tables in the database {database}:")
        for table in tables:
            print(table[0])
        
        conn.close()

    def print_column_names(self, database, table):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        
        print(f"Columns in the table '{table}':")
        for column in columns:
            print(f"Name: {column[1]}, Type: {column[2]}")
        
        conn.close()

if __name__ == "__main__":
    q = Queries()
    
    # Create Database
    database = r"databases\Attentiface.db"
    q.create(database, "Credentials", 
                columns = ["ID INTEGER PRIMARY KEY AUTOINCREMENT",
                            "gmail_address varchar(45) NOT NULL", 
                            "gmail_api_code varchar(45) NOT NULL"])
    
    # Create Schedule Table
    q.create(database, "Schedule",
                columns = ["ID INTEGER PRIMARY KEY AUTOINCREMENT",
                            "start_time varchar(45) NOT NULL", 
                            "end_time varchar(45) NOT NULL",
                            "break_time varchar(45) NOT NULL" ])
    
    # Create Employee Table
    q.create(database, "Employee",
                columns = ["ID INTEGER PRIMARY KEY AUTOINCREMENT",
                            "last_name varchar(45) NOT NULL", 
                            "first_name varchar(45) NOT NULL",
                            "middle_initial varchar(45) NOT NULL",
                            "gender varchar(45) NOT NULL",
                            "email varchar(45) NOT NULL",
                            "phone_number varchar(45) NOT NULL",
                            "address varchar(45) NOT NULL",
                            "photo_last_taken varchar(45) NOT NULL",
                            "employee_id varchar(45) NOT NULL" ])
    
    # Create Attendance Table
    q.create(database, "Attendance",
                columns = ["ID INTEGER PRIMARY KEY AUTOINCREMENT",
                           "employee_id varchar(45) NOT NULL",
                            "last_name varchar(45) NOT NULL", 
                            "first_name varchar(45) NOT NULL",
                            "middle_initial varchar(45) NOT NULL",
                            "time_in text",
                            "time_out text",
                            "date text",
                            "secondary_id text"
                             ])
    
    q.print_all_tables(database)
    q.print_column_names(database, "Credentials")
    q.print_column_names(database, "Schedule")
    q.print_column_names(database, "Employee")
    q.print_column_names(database, "Attendance")
