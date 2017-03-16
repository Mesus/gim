#coding=utf8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
channel = connection.channel()

channel.queue_declare(queue='x')

channel.basic_publish(exchange='', routing_key='x', body='r')
print " [x] Sent 'Hello World!'"
connection.close()

