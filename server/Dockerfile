FROM python:3.10-slim

WORKDIR /app

COPY soap_server.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-u", "soap_server.py"]