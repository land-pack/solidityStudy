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
from pysol import wallet


c = tornadoredis.Client()
c.connect()



class CreateAccountHandler(tornado.web.RequestHandler):
    def post(self):
        """
        {"passwd":123456}
        """
        passwd = self.get_argument('passwd')
        addr = wallet.create_account(str(passwd))
        self.set_header('Content-Type', 'text/plain')
        response = {
			"status": 200,
			"message": "ok",
			"data":{
				"address": addr
			}
		}
        self.write(response)
