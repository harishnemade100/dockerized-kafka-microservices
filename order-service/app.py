from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("🛒 Order Service Started")

while True:
    order_id = input("Enter Order ID (or exit): ")
    if order_id.lower() == "exit":
        break

    order = {"order_id": order_id, "status": "CREATED"}
    producer.send("orders-topic", order)
    producer.flush()
    print("✅ Order sent")
