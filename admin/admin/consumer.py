import pika, json
from products.models import Product

params = pika.URLParameters('amqps://YOUR_AMQP_USER:YOUR_AMQP_PASSWORD@toad.rmq.cloudamqp.com/YOUR_AMQP_USER')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    product_id = json.loads(body)
    product = Product.objects.get(id=product_id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')



channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

channel.close()