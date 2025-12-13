from kafka import KafkaConsumer, KafkaProducer
import json
import time

consumer = KafkaConsumer(
    "orders-topic",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="payment-group",
    auto_offset_reset="earliest"
)

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("💳 Payment Service Listening")

for msg in consumer:
    order = msg.value
    print("💰 Processing payment for", order["order_id"])
    time.sleep(2)

    payment = {"order_id": order["order_id"], "status": "PAID"}
    producer.send("payments-topic", payment)
    producer.flush()
