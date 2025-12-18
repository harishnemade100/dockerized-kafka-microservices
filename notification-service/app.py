from kafka import KafkaConsumer
import json
import time


print("📩 Notification Service Started", flush=True)


time.sleep(5)


consumer = KafkaConsumer(
    "payments",
    bootstrap_servers="kafka:9092",
    group_id="notification-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )


for msg in consumer:
    order_id = msg.value
    print(f"📢 Notification sent for Order {order_id} (Payment Success)", flush=True)