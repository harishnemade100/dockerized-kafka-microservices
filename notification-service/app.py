from kafka import KafkaConsumer
import json
import time


print("📩 Notification Service Started", flush=True)


time.sleep(5)

# Kafka Consumer Configuration
"""
Consumer configuration for the notification service.
- Topic: payments
- Bootstrap Servers: kafka:9092
- Group ID: notification-group
- Auto Offset Reset: earliest
- Value Deserializer: JSON
"""
consumer = KafkaConsumer(
    "payments",
    bootstrap_servers="kafka:9092",
    group_id="notification-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

"""
Main loop to consume messages from the 'payments' topic and send notifications.
Each message contains an order ID for which a payment was successful.
"""
for msg in consumer:
    order_id = msg.value
    print(f"📢 Notification sent for Order {order_id} (Payment Success)", flush=True)