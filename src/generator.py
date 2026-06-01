from faker import Faker

fake = Faker()


def generate_order():
    return {
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "amount": round(fake.pyfloat(
            left_digits=4,
            right_digits=2,
            positive=True
        ), 2)
    }