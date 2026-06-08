# FulfillSight

A data engineering learning project that simulates order generation and persistence using Docker and PostgreSQL.

## Overview

FulfillSight generates synthetic order data and stores it in a PostgreSQL database running inside Docker.

The project is being built incrementally to learn real-world data engineering concepts including:

* Python application development
* Docker containerization
* Docker Compose orchestration
* PostgreSQL integration
* Kafka event streaming (upcoming)
* Data pipelines and analytics (upcoming)

## Current Architecture
    Event Generator
        │
        ▼
    PostgreSQL

    Upcoming architecture:

    Event Generator
        │
        ▼
        Kafka
        │
        ▼
    PySpark Streaming
        │
        ▼
    PostgreSQL
        │
        ▼
        FastAPI
## Tech Stack
     Python 3.13
    PostgreSQL 17
    Docker
    Docker Compose
    Faker
    psycopg2

    Upcoming:

    Apache Kafka
    PySpark Structured Streaming
    FastAPI
    Database Schema
    order_events

    Stores raw immutable event history.

    warehouse_metrics

    Stores Spark-generated warehouse analytics.

    anomalies

    Stores operational alerts and anomaly detections.

    inventory_state

    Stores current inventory snapshots.

Event Contract

Every event in FulfillSight follows a standard schema:

{
  "event_id": "uuid",
  "event_type": "payment_failed",
  "order_id": "ORD_123",
  "warehouse_id": "WH_HYD_01",
  "sku_id": "SKU_0001",
  "quantity": 2,
  "amount": 499.99,
  "status": "pending",
  "event_timestamp": "2026-06-07T10:00:00Z"
}

## Features Implemented

### Day 1

* Synthetic order generation
* JSON output

### Day 2

* Docker fundamentals
* Docker image creation
* Container execution

### Day 3

* Docker Compose
* Environment variable management
* PostgreSQL container
* Database connectivity
* Orders table creation
* Order persistence

## Running the Project

### Build and Start

docker compose up --build

### Verify Stored Orders

docker exec -it fulfillsight_postgres psql -U ordersuser -d ordersdb

Inside PostgreSQL:

SELECT COUNT(*) FROM orders;

## Progress
### Completed
Synthetic order generation
Docker containerization
Docker Compose orchestration
Environment variable management
PostgreSQL integration
Automatic database initialization
Database schema design
Event contract definition
Repository refactor for future services
### In Progress
Kafka integration
### Planned
Kafka producers
Kafka consumers
PySpark Structured Streaming
Real-time analytics
FastAPI dashboard
Anomaly detection



## Learning Milestones

* [x] Generate synthetic order data
* [x] Containerize Python application
* [x] Docker Compose orchestration
* [x] Environment variable management
* [x] PostgreSQL container setup
* [x] PostgreSQL connectivity via psycopg2
* [x] Orders persisted to database
* [ ] Kafka producer
* [ ] Kafka consumer
* [ ] Event streaming pipeline
* [ ] Analytics layer

