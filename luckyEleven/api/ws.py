from __future__ import print_function
import sys
sys.path.append("..")

import datetime
import tornado.httpserver
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.gen
import tornadoredis
import ujson


from model.order import Luckyeleven
from pysol import rpc
from config.basic import publish_channel


c = tornadoredis.Client()
c.connect()

def lst_to_dict(lst, key=5):
    return {i[key]:i for i in lst} 

class MessageHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        yield tornado.gen.Task(self.client.subscribe, publish_channel)
        self.client.listen(self.on_message)
    
    def open(self, *args, **kwargs):
        """
        Check top 20 record, and write it back to client!
        """
        with Luckyeleven() as db:
            lst = db.top_20()

            resp = {
                "msg_type":"init",
                "msg_code": 1001,
                "data":{
                    "top": lst,
                    "lastdraw":"2|4|5|7|10",
                    "expectid":"1803151010",
                    "account":12.2
                }
            }
            resp = ujson.dumps(resp)
            self.write_message(resp)

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
            self.client.unsubscribe(publish_channel)
            self.client.disconnect()

    def check_origin(self, origin):
        return True
