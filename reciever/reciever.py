import pika
import sys
import os
import psycopg2


def insert_number(con, num):
    cursor = con.cursor()
    intnum = int(num)
    if intnum % 2 == 0:
        cursor.execute("INSERT INTO even VALUES ("+str(intnum)+");")
    else:
        cursor.execute("INSERT INTO odd VALUES ("+str(intnum)+");")
    con.commit()


def main():

    db2connection = psycopg2.connect(
        host="postgres",
        dbname="numbers",
        user="postgres",
        password="docker")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='numbers')

    def callback(ch, method, properties, body):
        insert_number(db2connection, body)
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='numbers', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
