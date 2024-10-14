import json
import time

from confluent_kafka import Producer

# Kafka broker details - Use the Kafka service name defined in docker-compose
kafka_broker = (
    "kafka:9092"  # This should match your Kafka service name in docker-compose
)

file = "./data/yelp_academic_dataset_review.json"

# Kafka Producer configuration
producer_config = {"bootstrap.servers": kafka_broker}

# Create the Kafka Producer
producer = Producer(producer_config)


# Callback to handle delivery reports (success or failure)
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


# Function to read from the file and send to Kafka
def send_to_kafka():
    with open(file) as f:
        for line in f:
            try:
                # Read line from file and parse as JSON
                record = json.loads(line)

                # Send the message to Kafka topic 'delta-pipeline'
                producer.produce(
                    "delta-pipeline", value=json.dumps(record), callback=delivery_report
                )

                # Wait for messages to be delivered
                producer.flush()

                # Print the message and simulate delay
                print(f"Sent: {record}")
                time.sleep(10)  # Simulate delay for each message

            except Exception as e:
                print(f"Error sending data: {e}")


if __name__ == "__main__":
    send_to_kafka()
