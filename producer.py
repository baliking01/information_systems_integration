import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='colorQueue')

colors = ['RED', 'GREEN', 'BLUE']

while True:
    color = random.choice(colors)
    channel.basic_publish(exchange='', routing_key='colorQueue', body=color)
    print(f"Sent: {color}")
    time.sleep(1)