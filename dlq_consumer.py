import pika

def callback(ch, method, properties, body):
    print(f"Message '{body.decode()}' has not been processed")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='DLQ', durable=True)
channel.basic_consume(queue='DLQ', on_message_callback=callback, auto_ack=True)

print('Waiting for stats...')
channel.start_consuming()