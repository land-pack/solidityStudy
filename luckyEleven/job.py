import time
import ujson
import redis
from tornado import ioloop
# self config
from config.basic import publish_channel
from pysol.watch import watching
from utils.cache import set_current_expect


r = redis.Redis()


def push_expect():
    timeString  = time.strftime("%Y%m%d%H%M%S", time.localtime())
    expectid = timeString[2:-2]
    set_current_expect(expectid)
    data = {
            	"msg_type": "new",
            	"msg_code": 1002,
            	"data": {
            		"expectid": expectid,
            		"timer": 60 - int(timeString[-2:])
            	}
            }
    r.publish(publish_channel, ujson.dumps(data))


# Watch the place event! if succesful will got a callback
watching()



# Run ever 10 seconds!
ioloop.PeriodicCallback(push_expect, 10*1000).start()


# Engine start here
ioloop.IOLoop.instance().start()
