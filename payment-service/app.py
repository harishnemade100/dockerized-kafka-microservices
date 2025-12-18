from kafka import KafkaConsumer, KafkaProducer
import json
import time


print("💳 Payment Service Started", flush=True)


time.sleep(5)

# Kafka Consumer Configuration
"""
Consumer configuration for the payment service.
- Topic: orders
- Bootstrap Servers: kafka:9092
- Group ID: payment-group
- Auto Offset Reset: earliest
- Value Deserializer: JSON
"""
consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="kafka:9092",
    group_id="payment-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

# Kafka Producer Configuration

"""
Producer configuration for the payment service.
- Bootstrap Servers: kafka:9092
- Value Serializer: JSON
"""
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

"""
Main loop to process orders from the 'orders' topic and send payment confirmations.
Each message contains an order ID for which payment needs to be processed.
"""
for msg in consumer:
    order_id = msg.value
    print(f"💰 Processing payment for Order {order_id}", flush=True)
    time.sleep(1)
    producer.send("payments", order_id)