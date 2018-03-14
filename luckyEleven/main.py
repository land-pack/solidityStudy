
import tornado.httpserver
import tornado.ioloop

# Import API
from api.order import MainHandler
from api.order import PlaceApiHandler
from api.order import NewMessageHandler
from api.order import MessageHandler


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
