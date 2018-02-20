import psycopg2


def connect():
    try:
        connect_str = "dbname='graduate_db' user='graduate' host='localhost' " + \
                      "password='graduate'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def create_table(cursor):
    cursor.execute("CREATE TABLE classifier_table (id serial primary key,average_duration_p jsonb,"
                   "average_sattering_q jsonb, average_dispersion_h);")
    cursor.execute("CREATE TABLE set_table (id serial PRIMARY KEY, );")


connect()
