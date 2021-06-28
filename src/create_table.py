import psycopg2
from config import config

def create_tables():
    """
    create tables in the pgSQL database
    :return:
    """

    commands = (
        """
        DROP TABLE IF EXISTS places;
        CREATE TABLE places (
            place_address_identity VARCHAR(255) PRIMARY KEY,
            longitude NUMERIC,
            latitude NUMERIC,
            city VARCHAR(255),
            state_abbreviation VARCHAR(255),
            postal_code VARCHAR(255)
        )
        """,
        """
        DROP TABLE IF EXISTS questions;
        CREATE TABLE questions (
            question_key BIGINT PRIMARY KEY,
            full_text VARCHAR,
            question_type VARCHAR(255)
        )
        """,
        """
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            source_bee_identity	VARCHAR(255),
            account_creation_date	TIMESTAMP WITHOUT TIME ZONE,
            activation_date	TIMESTAMP WITHOUT TIME ZONE,
            gender	VARCHAR(255)
        )
        """,
        """
        DROP TABLE IF EXISTS response_answers;
        CREATE TABLE response_answers (
            mission_identity	TEXT,
            pin_identity	VARCHAR(255),
            place_address_identity	VARCHAR(255),
            organization_name	VARCHAR(255),
            bee_identity	VARCHAR(255),
            customer_reporting_period	VARCHAR(255),
            customer_reporting_period_start	TIMESTAMP WITHOUT TIME ZONE,
            customer_reporting_period_end	TIMESTAMP WITHOUT TIME ZONE,
            mission_response_identity	VARCHAR(255),
            utc_started_at	TIMESTAMP WITHOUT TIME ZONE,
            local_started_at	TIMESTAMP WITHOUT TIME ZONE,
            utc_submitted_at	TIMESTAMP WITHOUT TIME ZONE,
            local_submitted_at	TIMESTAMP WITHOUT TIME ZONE,
            submitted_latitude	NUMERIC,
            submitted_longitude	NUMERIC,
            mission_reward_points	INTEGER,
            mission_response_status	VARCHAR(255),
            result_response_id	BIGINT,
            question_identity	BIGINT,
            question_position_identifier	VARCHAR(255),
            response_answer	TEXT
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