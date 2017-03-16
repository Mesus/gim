import pika
def callback(ch, method, properties, body):
  print " [x] Received %r" % (body,)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
channel = connection.channel()

channel.basic_consume(callback, queue='x', no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
connection.close()