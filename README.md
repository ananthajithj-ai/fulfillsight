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

## Architecture

Python Application Container

↓

PostgreSQL Container

↓

Orders Table

The Python service generates fake order records and inserts them into PostgreSQL using psycopg2.

## Tech Stack

* Python 3.13
* Docker
* Docker Compose
* PostgreSQL 17
* Faker
* psycopg2

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

## Current Status

Completed:

* Dockerized application
* PostgreSQL integration
* Order persistence

Planned:

* Kafka producer
* Kafka consumer
* Event streaming pipeline
* Analytics layer

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

