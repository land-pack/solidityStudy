

# std lib
import logging


# Tornado lib
import tornado.httpserver
import tornado.ioloop

# Import API
from api.order import MainHandler
from api.order import PlaceApiHandler
from api.order import TestMessageHandler
from api.order import MyOrderHandler

# For wallet
from api.wallet import CreateAccountHandler
from api.wallet import MyAccountHandler

# For WebSocket
from api.ws import MessageHandler


# ============ Log configuration =========
#handler = logging.FileHandler(log_file_filename)
#logger.addHandler(handler)
#logger.setLevel(logging.INFO)




# Map api
application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/order/place', PlaceApiHandler),
    (r'/my/his', MyOrderHandler),
    (r'/test/input', TestMessageHandler),
    (r'/ws/track', MessageHandler),
    (r'/account/create', CreateAccountHandler),
    (r'/account/info', MyAccountHandler)
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print('Demo is runing at 0.0.0.0:8888\nQuit the demo with CONTROL-C')
    tornado.ioloop.IOLoop.instance().start()
