import pika, sys, os




def callback(ch, method, properties, body):
    print("Received message:", body.decode('utf-8'))


# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declare the queue to consume from
channel.queue_declare(queue='my_queue')

# Set up the callback function
channel.basic_consume(queue='queue', on_message_callback=callback, auto_ack=True)

# Start consuming messages
print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
