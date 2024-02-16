import sqlite3, json

class Database:
    def __init__(self, path_to_date='main.db'):
        self.path_to_date = path_to_date


    @property
    def connection(self):
        return sqlite3.connect(self.path_to_date)
    

    def execute(self, sql: str, parametrs: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    

    def create_data_user(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        );
        """
        self.execute(sql, commit=True)
        self.create_data_participants()


    def create_data_participants(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Participants (
        user_id INTEGER,
        follower_ids TEXT,
        PRIMARY KEY (user_id)
        );
        """
        self.execute(sql, commit=True)


    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += "AND".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())
        

    def add_user(self, id: int, name: str):
        sql = "INSERT INTO Users (id, name) VALUES (?, ?)"
        self.execute(sql, parametrs=(id, name), commit=True)


    def select_all_users(self):

        sql ="""
        SELECT * FROM Users
        """
        
        return self.execute(sql, fetchall=True)


    def select_user(self, **kwargs):
        
        sql = "SELECT * FROM Users WHERE"
        sql, parametrs = self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parametrs, fetchone=True)
    
    def delete_user(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def add_follower(self, user_id: int, follower_id: int):
        current_followers = set(self.get_followers_list(user_id))
        current_followers.add(follower_id)
        follower_ids_json = json.dumps(list(current_followers))
        sql = "INSERT OR REPLACE INTO Participants (user_id, follower_ids) VALUES (?, ?)"
        self.execute(sql, parametrs=(user_id, follower_ids_json), commit=True)



    def count_followers(self, user_id: int) -> int:
        followers_list = self.get_followers_list(user_id)
        return len(followers_list)

    def get_followers_list(self, user_id: int) -> list:
        sql = "SELECT follower_ids FROM Participants WHERE user_id=?"
        followers_json = self.execute(sql, parametrs=(user_id,), fetchone=True)
        if followers_json and followers_json[0]:
            return json.loads(followers_json[0])
        else:
            return []






def logger(statement):
    print(f"""
------------------------
Executing:
{statement}
------------------------
""")

