from kafka import KafkaConsumer, KafkaProducer
import json
import time


print("💳 Payment Service Started", flush=True)


time.sleep(5)


consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="kafka:9092",
    group_id="payment-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )


producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


for msg in consumer:
    order_id = msg.value
    print(f"💰 Processing payment for Order {order_id}", flush=True)
    time.sleep(1)
    producer.send("payments", order_id)