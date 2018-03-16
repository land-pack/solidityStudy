
import redis


from config.basic import redis_host
from config.basic import REDIS_PREFIX
from config.basic import REDIS_ORDER_BLOCK
from config.basic import REDIS_EXPECT_ORDER
from config.basic import REDIS_CLOCK_FLAG

r = redis.Redis(redis_host)


def push_user_place_hash(expectid, hx):
    """
    The key is end with expect id
    """
    print("expectid={} || hx={}".format(expectid, hx))
    r.rpush(REDIS_EXPECT_ORDER.format(expectid), hx)

def pop_by_hx(expectid, hx):
    r.lrem(REDIS_EXPECT_ORDER.format(expectid), hx)

def left_hx(exid=0):
    d = r.lrange(REDIS_EXPECT_ORDER.format(exid), 0, -1)
    print(d)
    return d

def is_finish_order(expectid):
    d = r.llen(REDIS_EXPECT_ORDER.format(expectid))
    return d == 0
 
def is_current_time_over(ex):
    return r.exists(REDIS_CLOCK_FLAG.format(ex))


def set_current_expect(expectid):
    """
    Set current expectid
    """
    r.set(REDIS_PREFIX.format('current_expect'), expectid)
    r.expire(REDIS_PREFIX.format('current_expect'), 100*3600)
    
    # Set current expect max time limit (default 60 seconds)
    r.set(REDIS_CLOCK_FLAG, 1, ex=60)

def get_current_expect_id():
    """
    Return current expect id 
    """
    return r.get(REDIS_PREFIX.format("current_expect"))


def push_block(expectid=0, blockid=0):
    print("the blockid type={} --  blockid={}".format(type(blockid), blockid))
    r.rpush(REDIS_ORDER_BLOCK.format(str(expectid)), str(blockid))
    r.expire(REDIS_ORDER_BLOCK.format(str(expectid)), 60 * 1000)


def top_block(expectid=get_current_expect_id()):
    block_lst = r.lrange(REDIS_ORDER_BLOCK.format(str(expectid)), 0, -1) or []
    print("block_lst=={}".format(block_lst))
    block_lst = sorted(block_lst, reverse=True)
    print(block_lst)
    return  block_lst[0] if block_lst else 0
