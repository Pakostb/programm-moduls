import pymysql
import pymysql.cursors


class Database:
    def __init__(self, host='localhost', user='root', password='admin', database='flask_auth'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )

    def create_user(self, name, password):
        """INSERT пользователя. Возвращает lastrowid или бросает исключение при дубле."""
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (user_name, user_password) VALUES (%s, %s)",
                (name, password)
            )
        self.conn.commit()
        return cur.lastrowid

    def get_user(self, name):
        """Найти пользователя по имени."""
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM users WHERE user_name = %s",
                (name,)
            )
            return cur.fetchone()

    def close(self):
        self.conn.close()
