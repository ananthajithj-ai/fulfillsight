import json
import logging
import os
from db.db import (
    get_connection,
    create_orders_table,
    insert_order
)
from shared.config import APP_NAME,TOTAL_RECORDS,LOG_LEVEL
from event_generator.generator import generate_order

# Create directories if they don't exist
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("data", exist_ok=True)

conn = get_connection()
print("Connected to Postgres")
conn.close()
create_orders_table()
print("Orders table ready")

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting order generation")

orders = []

for _ in range(int(TOTAL_RECORDS)):
    order = generate_order()

    orders.append(order)

    insert_order(order)

logging.info(f"Generated {len(orders)} orders")

with open("data/orders.json", "w") as file:
    json.dump(orders, file, indent=4)

logging.info("Successfully wrote orders to data/orders.json")

print(f"Generated {len(orders)} Orders")
print(f"APP_NAME = {APP_NAME}")
print(f"TOTAL_RECORDS = {TOTAL_RECORDS}")
print(f"LOG_LEVEL = {LOG_LEVEL}")