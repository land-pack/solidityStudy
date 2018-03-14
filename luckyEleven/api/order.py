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
            "digit_curreny": "2000"
        },
        {
            "user_addr": "0x627306090abab3a6e1400e9345bc60c78a8bef57",
            "expect_id": "1803120252",
            "lucky_num": "02|03|05|08|09",
            "digit_curreny": "1000"
        }]
        """
        message = self.get_argument("message")
        data = ujson.loads(message)
        # RPC
        tx_lst = {}
        

        for i in data:
            order_status = 0
            with Luckyeleven() as db:
                tx = db.place(i.get("user_addr"),
                         i.get("expect_id"),
                         i.get("lucky_num"),
                         i.get("digit_curreny"),
                         0, # result
                         order_status) # status

                tx_lst[tx] = {
                    "place_time": str(datetime.timedelta(seconds=666)),
                    "user_addr": i.get("user_addr"),
                    "expect_id": i.get("expect_id"),
                    "lucky_num": i.get("lucky_num"),
                    "digit_curreny": i.get("digit_curreny"),
                    "prize_result": order_status,
                    "lucky_result": "" # if value is empty, you should ignore this
                }
        self.write("place transacrion >>{}".format(tx_lst))
        c.publish('test_channel', ujson.dumps(tx_lst))




