
import tornado.httpserver
import tornado.ioloop

# Import API
from api.order import MainHandler
from api.order import PlaceApiHandler
from api.order import NewMessageHandler

# For wallet
from api.wallet import CreateAccountHandler

# For WebSocket
from api.ws import MessageHandler

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/order/place', PlaceApiHandler),
    (r'/msg', NewMessageHandler),
    (r'/ws/track', MessageHandler),
    (r'/account/create', CreateAccountHandler)
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print('Demo is runing at 0.0.0.0:8888\nQuit the demo with CONTROL-C')
    tornado.ioloop.IOLoop.instance().start()
