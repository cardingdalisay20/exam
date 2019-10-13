import psycopg2
# from  psycopg2 import Error


# noinspection PyUnboundLocalVariable
class Record:
        def __init__(self):
            pass

        host = "127.0.0.1"
        user = "postgres"
        password = ""
        port = "5432"
        database = "boholtours"

        @staticmethod
        def initConnect():
            connection = psycopg2.connect(user=Record.user,
                                          password="",
                                          host=Record.host,
                                          port=Record.port,
                                          database=Record.database)
            return connection

        @staticmethod
        def checkConnection():
            try:
                conn = Record.initConnect()
                cur = conn.cursor()
                create_table_query = '''CREATE TABLE mobile (ID INT PRIMARY KEY NOT NULL, MODEL TEXT NOT NULL, PRICE REAL); '''
                cur.execute(create_table_query)
                conn.commit()
                print("Table created successfully in PostgreSQL ")
            except (Exception, psycopg2.DatabaseError) as error:
                print ("Error while creating PostgreSQL table", error)
            finally:
            # closing database connection.
                if conn:
                    cur.close()
                    conn.close()
                    print("PostgreSQL connection is closed")

        @staticmethod
        def runQuery(sql):
            try:
                conn = Record.initConnect()
                cur = conn.cursor()
                query = '''{}'''.format(sql)
                cur.execute(query)
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
            # closing database connection.
                if conn:
                    cur.close()
                    conn.close()

        @staticmethod
        def fetchAllRecord(sql):
            try:
                conn = Record.initConnect()
                cur = conn.cursor()
                query = '''{}'''.format(sql)
                cur.execute(query)
                record = cur.fetchall()
                conn.commit()

                return record
            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
            # closing database connection.
                if conn:
                    cur.close()
                    conn.close()

        @staticmethod
        def fetchSingleRecord(sql):
            try:
                conn = Record.initConnect()
                cur = conn.cursor()
                query = '''{}'''.format(sql)
                cur.execute(query)
                record = cur.fetchone()
                conn.commit()

                return record

            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
                # closing database connection.
                if conn:
                    cur.close()
                    conn.close()



