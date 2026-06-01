import json
import logging
from src.config import TOTAL_RECORDS
from src.generator import generate_order


logging.basicConfig(
    filename = "logs/app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Starting order generation");

orders = []

for _ in range(int(TOTAL_RECORDS)):
    orders.append(generate_order())


logging.info(f"Generated {len(orders)} orders")


with open("data/orders.json","w") as file:
    json.dump(orders,file,indent = 4)


logging.info("Successfully wrote orders to data/orders.json")



print(f"Generated {len(orders)} Orders")