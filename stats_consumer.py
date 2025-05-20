import pika

def callback(ch, method, properties, body):
    print(f"10 '{body.decode()}' messages have been processed")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='colorStatistics', durable=True)
channel.basic_consume(queue='colorStatistics', on_message_callback=callback, auto_ack=True)

print('Waiting for stats...')
channel.start_consuming()