import time
import ujson
import redis
from tornado import ioloop
# self config
from config.basic import publish_channel
    

r = redis.Redis()


def hello():
	print("hello")

ioloop.PeriodicCallback(hello, 10*1000).start()



def push_expect():
    timeString  = time.strftime("%Y%m%d%H%M%S", time.localtime())
    data = {
            	"msg_type": "new",
            	"msg_code": 1002,
            	"data": {
            		"expectid": timeString[2:-2],
            		"timer": 60 - int(timeString[-2:])
            	}
            }
    r.publish(publish_channel, ujson.dumps(data))

ioloop.PeriodicCallback(push_expect, 5*1000).start()
ioloop.IOLoop.instance().start()
