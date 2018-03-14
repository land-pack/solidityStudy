from __future__ import print_function
import tornado.httpserver
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.gen

import tornadoredis
import ujson


from dbs import Luckyeleven
from pysol import rpc


c = tornadoredis.Client()
c.connect()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template.html", title="PubSub + WebSocket Demo")


class NewMessageHandler(tornado.web.RequestHandler):
    def post(self):
        message = self.get_argument('message')
        c.publish('test_channel', message)
        self.set_header('Content-Type', 'text/plain')
        self.write('place successful :)')


class PlaceApiHandler(tornado.web.RequestHandler):

    def post(self):
        """
        [{
            "user_addr": "0x627306090abab3a6e1400e9345bc60c78a8bef57",
            "expect_id": "1803120252",
            "lucky_num": "02|03|05|08|09",
            "digit_curreny": "0.000221"
        },
        {
            "user_addr": "0x627306090abab3a6e1400e9345bc60c78a8bef57",
            "expect_id": "1803120252",
            "lucky_num": "02|03|05|08|09",
            "digit_curreny": "0.000221"
        }]
        """
        message = self.get_argument("message")
        data = ujson.loads(message)
        # RPC
        tx_lst = []
        for i in data:
            with Luckyeleven() as db:
                print('i --{}'.format(i))
                tx = db.place(i.get("user_addr"),
                         i.get("expect_id"),
                         i.get("lucky_num"),
                         i.get("digit_curreny"),
                         0, # result
                         0) # status
                tx_lst.append(tx)
        self.write("place transacrion >>{}".format(tx_lst))



class MessageHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        yield tornado.gen.Task(self.client.subscribe, 'test_channel')
        self.client.listen(self.on_message)

    def on_message(self, msg):
        if msg.kind == 'message':
            self.write_message(str(msg.body))
        if msg.kind == 'disconnect':
            # Do not try to reconnect, just send a message back
            # to the client and close the client connection
            self.write_message('The connection terminated '
                               'due to a Redis server error.')
            self.close()

    def on_close(self):
        if self.client.subscribed:
            self.client.unsubscribe('test_channel')
            self.client.disconnect()

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/place', PlaceApiHandler),
    (r'/msg', NewMessageHandler),
    (r'/track', MessageHandler),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print('Demo is runing at 0.0.0.0:8888\nQuit the demo with CONTROL-C')
    tornado.ioloop.IOLoop.instance().start()
