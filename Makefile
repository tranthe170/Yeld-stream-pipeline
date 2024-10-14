# Commands to manage individual services
.PHONY: all minio spark kafka hive producer trino superset up down logs clean

# Start all services
all: up

# Start the MinIO service
minio:
	docker-compose up -d minio mc

# Start the Hive services (Metastore and MySQL)
hive:
	docker-compose up -d mysql hive-metastore

# Start the Spark services (master and workers)
spark:
	docker-compose up -d spark-master spark-worker jupyter-notebook

# Start the Kafka services (Zookeeper and Kafka brokers)
kafka:
	docker-compose up -d zookeeper kafka
	@echo "Waiting for Kafka to become ready..."
	sleep 5
	docker-compose up -d kafka-schema-registry conduktor-platform

# Start the Kafka Producer service
producer:
	docker-compose up -d producer

# Stop the Kafka Producer service
producer-stop:
	docker-compose stop producer

# Start the Trino services (Coordinator and Workers)
trino:
	docker-compose up -d trino-coordinator trino-worker

# Start the Superset service
superset:
	docker-compose up -d postgres-superset superset

# Bring up all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Show logs for all services
logs:
	docker-compose logs -f

# Clean up the compose file
clean:
	rm -f docker-compose.yml
