import time
import ujson
import redis
from tornado import ioloop
# self config
from config.basic import publish_channel
from pysol.watch import watching
    

r = redis.Redis()


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


# Watch the place event! if succesful will got a callback
watching()



# Run ever 1 minute!
ioloop.PeriodicCallback(push_expect, 60*1000).start()


# Engine start here
ioloop.IOLoop.instance().start()
