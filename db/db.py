import psycopg2
from psycopg2.extras import Json
from shared.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    return conn


def create_orders_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        order_data JSONB NOT NULL
    )
    """)

    conn.commit()

    cursor.close()
    conn.close()

    
def insert_order(order):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO orders (order_data)
        VALUES (%s)
        """,
        (Json(order),)
    )

    conn.commit()

    cursor.close()
    conn.close()