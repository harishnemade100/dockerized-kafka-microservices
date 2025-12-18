from kafka import KafkaProducer
import json
import time


print("🛒 Order Service Started", flush=True)


time.sleep(5)

# Kafka Producer Configuration
"""
Producer configuration for the order service.
- Bootstrap Servers: kafka:9092
- Value Serializer: JSON

"""
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


while True:
    order_id = input("Enter Order ID (or exit): ").strip()