# Python Message Gateway API

Based on Python UV Template

Consumes a message from a RabbitMQ queue and forwards to a Firestore collection

## Setup

- Create a .env file with the following entry:

        CLOUDAMQP_URL=amqp://[your credentials]

- Create a .json file that contains your Firestore credentials.

## Dependencies (already added, see *uv.lock*)

⚠️ CloudAMQP docs recommends Pika version == 1.1.0 

```
uv add pika==1.1.0
uv add python-dotenv
uv add firebase-admin
```

## Running

```
uv run python consumer.py
```

