import psycopg2
from config import config
from catalog import catalog

def insert_event_finance_customer_order_line_items_table():
    """
    insert multiple rows of the csv into the table
    :return:
    """
    # sql = ''
    conn = None
    with open(catalog['to_ingest/event_finance_customer_order_line_items'], 'r') as event_finance_customer_order_line_items:
        try:
            # read database configuration
            params = config()
            # connect to the pgSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            next(event_finance_customer_order_line_items) # skip the header row.
            cur.copy_expert("""COPY event_finance_customer_order_line_items FROM STDIN WITH (FORMAT CSV)""", event_finance_customer_order_line_items)
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        event_finance_customer_order_line_items.close()

if __name__ == '__main__':
    insert_event_finance_customer_order_line_items_table()