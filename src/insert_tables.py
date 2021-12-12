import psycopg2
from config import config
from catalog import catalog
from loader import Loader

def insert_table(tablename=None):
    """
    insert multiple rows of the csv into the table
    :return:
    """

    conn = None
    with open(catalog[f"to_ingest/{tablename}"], 'r') as t:
        try:
            # determine file format
            file_format = t.name.split('.')[-1]

            # read database configuration
            params = config()
            # connect to the pgSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            next(t) # skip the header row.
            loader = Loader(curser=cur, table=t, tablename=tablename, format=file_format)
            cur = loader.load()
            # load(curser=cur, table=t, format='csv')
            # cur.copy_expert(f"""COPY {table} FROM STDIN WITH (FORMAT CSV)""", t)
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
    insert_table(tablename="places")
    insert_table(tablename="questions")
    insert_table(tablename="response_answers")
    insert_table(tablename="users")