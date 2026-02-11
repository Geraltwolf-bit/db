import psycopg2

def connect_database():
    try:
        conn = psycopg2.connect(
        host="",
        database="",
        user="",
        password=''
)
        
        print('Connected successfully')
        return conn
    
    except Exception as e:
        print(f'Error connecting to database: {e}')
        return None
    

connect_database()