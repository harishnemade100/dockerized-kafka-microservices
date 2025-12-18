import time
from kafka import KafkaAdminClient

def wait_for_kafka():
    while True:
        try:
            KafkaAdminClient(bootstrap_servers="kafka:9092")
            print("✅ Kafka is ready")
            break
        except Exception:
            print("⏳ Waiting for Kafka...")
            time.sleep(5)
