from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "payments-topic",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="notification-group",
    auto_offset_reset="earliest"
)

print("📩 Notification Service Listening")

for msg in consumer:
    payment = msg.value
    print(
        f"📢 Notification sent for Order {payment['order_id']} (Payment Success)"
    )
