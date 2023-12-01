import pika, json

params = pika.URLParameters('amqps://YOUR_AMQP_USER:YOUR_AMQP_PASSWORD@toad.rmq.cloudamqp.com/YOUR_AMQP_USER')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)