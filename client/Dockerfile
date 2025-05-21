FROM python:3.12-slim

WORKDIR /app

COPY soap_client.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "soap_client.py"]