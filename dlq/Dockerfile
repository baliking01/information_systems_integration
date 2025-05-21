FROM python:3.12-slim

WORKDIR /app

COPY dlq_consumer.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "dlq_consumer.py"]