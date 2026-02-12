import psycopg2
import traceback

def connect_db():
    try:
        conn = psycopg2.connect(
            host="5.129.202.223",
            database="default_db",
            user="gen_user",
            password="Geraltwolf7784681!",
            port="5432",
            sslmode="require"
        )
        print("Database connected")
        return conn

    except Exception as e:
        print(f"Error connecting to database: {e}")
        print(f"Error type: {type(e).__name__}")
        traceback.print_exc()
        return None