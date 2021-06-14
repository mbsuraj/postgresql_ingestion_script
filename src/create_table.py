import psycopg2
from config import config

def create_tables():
    """
    create tables in the pgSQL database
    :return:
    """

    commands = (
        """
        DROP TABLE IF EXISTS event_finance_customer_order_line_items;
        CREATE TABLE event_finance_customer_order_line_items (
            id INTEGER NOT NULL PRIMARY KEY,
            customer_order_id VARCHAR(255) NOT NULL,
            event_id INTEGER NOT NULL,
            event_type VARCHAR(255) NOT NULL,
            line_item_id VARCHAR(255) NOT NULL,
            deleted_at VARCHAR(255),
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the pgSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the pgSQL database
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()