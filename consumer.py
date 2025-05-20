import pika
import random

def callback(ch, method, properties, body, color):
    # dead letter, send to DLQ
    if random.randint(1, 10) <= 3:
        print(f"Dead: {color}")
        ch.basic_publish(exchange='',
                         routing_key='DLQ',
                         body=color)
    # process message, send to stats after 10
    else:
        print(f"processed: {color}")
        callback.processed[color] += 1
        if callback.processed[color] % 10 == 0:
            ch.basic_publish(exchange='',
                             routing_key='colorStatistics',
                             body=color)

callback.processed = {
    'RED': 0,
    'GREEN': 0,
    'BLUE': 0
}


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='colorExchange', exchange_type='direct', durable=True)

colors = ['RED', 'GREEN', 'BLUE']

for color in colors:
    channel.queue_declare(queue=color, durable=True)
    channel.queue_bind(exchange='colorExchange', queue=color, routing_key=color)

channel.queue_declare(queue='colorStatistics', durable=True)
channel.queue_declare(queue='DLQ', durable=True)

for color in colors:
    channel.basic_consume(queue=color, 
                          on_message_callback=lambda ch, method, properties, body, color=color: callback(ch, method, properties, body, color), 
                          auto_ack=True)

print('Waiting for color messages...')
channel.start_consuming()