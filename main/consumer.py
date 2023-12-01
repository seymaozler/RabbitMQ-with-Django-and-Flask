import pika, json
from sqlalchemy.orm import Session
from database import db
from schemas import ProductBase

params = pika.URLParameters('amqps://YOUR_AMQP_USER:YOUR_AMQP_PASSWORD@toad.rmq.cloudamqp.com/YOUR_AMQP_USER')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')



def callback(ch, method, properties, body):
    data = json.loads(body)
    if properties.content_type == 'product_created':
        product = ProductBase(id=data['id'], title=data['title'], image=data['image'], price=data['price'])
        db.add(product)
        db.commit()
    elif properties.content_type == 'product_updated':
        product = db.query(ProductBase).get(data['id'])
        product.title = data['title']
        product.image = data['image']
        product.price = data['price']
        db.commit()
    elif properties.content_type == 'product_deleted':
        product_id = int(data)
        product = db.query(ProductBase).get(id=product_id).first()
        db.delete(product)
        db.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()