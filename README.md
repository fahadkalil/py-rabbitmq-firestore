# Python Message Gateway API

Based on Python UV Template

Consumes a message from a RabbitMQ queue and forwards to a Firestore collection

## Running

```
uv run python consumer.py
```

## Dependencies (already added)

- ⚠️ CloudAMQP docs recommends Pika version == 1.1.0 

```
uv add pika==1.1.0
uv add python-dotenv
uv add firebase-admin
```

