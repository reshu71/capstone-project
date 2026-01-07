from  db_driver import PostgresDriver

class UserManager:
    def __init__(self,db_url):
        self._db = PostgresDriver(db_url)
        self._db.connect()
    def get_all_users(self):
        return self._db.execute_query("SELECT * FROM users")

if __name__=='__main__':
    x = UserManager('xyz.com')
    print(x.get_all_users())