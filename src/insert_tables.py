import psycopg2
from config import config
from catalog import catalog

def insert_table(table=None):
    """
    insert multiple rows of the csv into the table
    :return:
    """
    # sql = ''
    conn = None
    with open(catalog[f"to_ingest/{table}"], 'r') as t:
        try:
            # read database configuration
            params = config()
            # connect to the pgSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            next(t) # skip the header row.
            cur.copy_expert(f"""COPY {table} FROM STDIN WITH (FORMAT CSV)""", t)
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        t.close()

if __name__ == '__main__':
    insert_table(table="places")
    insert_table(table="questions")
    insert_table(table="response_answers")
    insert_table(table="users")