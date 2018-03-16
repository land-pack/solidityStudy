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
from pysol import rpc

c = tornadoredis.Client()
c.connect()



class CreateAccountHandler(tornado.web.RequestHandler):
    def post(self):
        """
        {"passwd":123456}
        """
        request_data = self.get_argument('request')
        request_data = ujson.loads(request_data)
        passwd = request_data.get("passwd")
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

class MyAccountHandler(tornado.web.RequestHandler):

    def post(self):
        """
        #If you have text/plain Content-Type, you should do it on the below way!
        curl -d 'request={"user_addr":"0x6f39Bb3dA74B402f35394196e997FdB793c624f7"}'  -X POST http://127.0.0.1:8888/account/info
        
        #If you run the application/json Content-Type, you should do it on the following way!

        """
        print(self.request.arguments)
        self.set_header('Content-Type', 'text/plain')
        #self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        request_data = self.get_argument('request')
        request_data = ujson.loads(request_data)
        user_addr = request_data.get("user_addr")
        account = rpc.get_balance(user_addr)
        print(account)
        eth_account = account /1000000
        with Luckyeleven() as db:
            ret =  db.fetch_order_by_addr(user_addr)
            order_lst = ret.get("data")
            counter = ret.get("counter")

        resp = {
            "status": 200,
            "message": "ok",
            "data": {
                "counter": counter,
                "account": eth_account or 0,
                "order_lst": order_lst
            }
        }
        #resp = ujson.dumps(resp)
        self.write(resp)
