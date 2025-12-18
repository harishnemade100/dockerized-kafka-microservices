from kafka import KafkaProducer
import json
import time


print("🛒 Order Service Started", flush=True)


time.sleep(5)


producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


while True:
    order_id = input("Enter Order ID (or exit): ").strip()


if order_id.lower() == "exit":
    break


if not order_id:
    print("⚠️ Order ID cannot be empty", flush=True)
    continue


    producer.send("orders", order_id)
    print(f"✅ Order {order_id} sent", flush=True)