import unittest
from main import main
import os
import ast
import json
from demjson import decode
import pika


def callback(channel, method_frame, properties, body):
    raise Exception(channel, method_frame, properties, body)


class TestFunctions(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "hello world")

    def test_fail(self):
        self.assertEqual(1, 5)

    def test_secure(self):
        # data = json.loads(json.dumps(os.environ['example']))
        # data = ast.literal_eval(os.environ['example'])
        data = decode(os.environ['example'])
        self.assertEqual(data['a'], 1)

    def test_rabbitmq(self):
        parameters = pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=pika.PlainCredentials('guest', 'guest'),
            virtual_host='/'
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)
        channel.basic_publish(
            exchange='',
            routing_key='test',
            body='text',
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        consumer_tag = channel.basic_consume(consumer_callback=callback, queue='test')
        channel.start_consuming()


if __name__ == '__main__':
    unittest.main()
