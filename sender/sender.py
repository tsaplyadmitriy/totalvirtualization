import pika
import random
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='numbers')

while True:
    nextint = random.randint(1, 100)
    time.sleep(2)

    channel.basic_publish(exchange='',
                          routing_key='numbers',
                          body=str(nextint))
    print(nextint)
