# 🚀 Dockerized Kafka Microservices (Orders → Payments → Notifications)

## 📌 Project Overview

This project demonstrates a **real-world, event-driven microservices architecture** using **Apache Kafka**, **Python**, and **Docker**. It simulates an e-commerce–style workflow where:

1. An **Order Service** produces order events
2. A **Payment Service** consumes orders and processes payments
3. A **Notification Service** consumes payment events and sends notifications

All services communicate **asynchronously via Kafka topics**, showcasing scalability, fault tolerance, and real-time processing.

---

## 🧠 Why Kafka?

Apache Kafka is a **distributed event streaming platform** used for building **real-time data pipelines** and **event-driven systems**.

### Kafka solves:

* Loose coupling between services
* High-throughput message processing
* Fault tolerance & replayability
* Horizontal scalability

In this project, Kafka acts as the **central event backbone** connecting independent microservices.

---

## 🏗️ Architecture

```
User Input (Terminal)
        ↓
Order Service (Producer)
        ↓  [orders topic]
Kafka Broker
        ↓
Payment Service (Consumer + Producer)
        ↓  [payments topic]
Kafka Broker
        ↓
Notification Service (Consumer)
```

---

## 📦 Tech Stack

* **Apache Kafka** – Event streaming
* **Zookeeper** – Kafka coordination
* **Python 3.10** – Service implementation
* **kafka-python** – Kafka client library
* **Docker & Docker Compose** – Containerization

---

## 📁 Project Structure

```
dockerized-kafka-microservices/
│
├── docker-compose.yml
│
├── order-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── payment-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── notification-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## 🔄 Kafka Topics

| Topic Name | Producer        | Consumer             |
| ---------- | --------------- | -------------------- |
| `orders`   | Order Service   | Payment Service      |
| `payments` | Payment Service | Notification Service |

---

## ⚙️ How It Works (Flow)

### 1️⃣ Order Service

* Takes live user input from terminal
* Publishes order ID as JSON to `orders` topic

### 2️⃣ Payment Service

* Subscribes to `orders`
* Simulates payment processing
* Publishes payment success to `payments` topic

### 3️⃣ Notification Service

* Subscribes to `payments`
* Displays real-time notifications

All services run independently and communicate **only through Kafka**.

---

## ▶️ How to Run the Project

### Prerequisites

* Docker
* Docker Compose

### Step 1: Start Services

```bash
docker-compose up --build
```

### Step 2: Open Terminals

**Order Input**

```bash
docker attach dockerized-kafka-microservices-order-service-1
```

Type:

```
101
102
103
```

**Payment Logs**

```bash
docker logs -f dockerized-kafka-microservices-payment-service-1
```

**Notification Logs**

```bash
docker logs -f dockerized-kafka-microservices-notification-service-1
```

You will see **live event flow across services**.

---

## 🔥 Key Kafka Concepts Demonstrated

* Producers & Consumers
* Consumer Groups
* Topic-based messaging
* Offset management
* Fault tolerance (restart services)
* Asynchronous communication

---

## 💡 Real-World Relevance

This architecture is commonly used in:

* E-commerce systems
* Payment gateways
* Logistics & tracking
* Real-time analytics
* Microservice-based enterprises

---

## 🧪 Fault Tolerance Demo

You can stop a service:

```bash
docker stop payment-service
```

Kafka retains messages, and when the service restarts, it **resumes from last offset**.

---

## 🧠 What I Learned / Experience Gained

* Designing event-driven systems
* Kafka internals (topics, partitions, offsets)
* Dockerizing Python microservices
* Debugging distributed systems
* Handling real-time data streams

---

## 🚀 Future Enhancements

* FastAPI REST endpoints
* Kafka UI (AKHQ / Confluent UI)
* Multiple brokers & partitions
* Schema Registry (Avro)
* AWS MSK deployment

---

## 👨‍💻 Author

**Harish Nemade**
Skilled Software Professional | Python | Data Engineering | Kafka | Docker

---

⭐ If you find this project helpful, give it a star and feel free to fork!
