import unittest
from main import main
import os
import ast
import json
from demjson import decode
from deepinfra.messaging.rabbitmq.rabbitmq import RabbitMQ


def callback(message, acknowledge, unacknowledge, delivery_tag, redelivered):
    raise Exception(message, acknowledge, unacknowledge, delivery_tag, redelivered)


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
        rabbit_mq = RabbitMQ([{'host':'', 'port':''}], 'guest', 'guest', '/')
        rabbit_mq.connect()
        rabbit_mq.send('test', 'this is a test')
        rabbit_mq.receive('test', callback)


if __name__ == '__main__':
    unittest.main()
