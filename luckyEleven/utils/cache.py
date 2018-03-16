
import redis


from config.basic import redis_host
from config.basic import REDIS_PREFIX


r = redis.Redis(redis_host)


def push_user_place_hash(expectid, hx):
    """
    The key is end with expect id
    """
    r.rpush(REDIS_PREFIX.format(expectid), hx)

def pop_by_hx(expectid, hx):
    r.lrem(REDIS_PREFIX.format(expectid), hx)

def left_hx(exid=0):
    d = r.lrange(REDIS_PREFIX.format(exid), 0, -1)
    print(d)
    return d

def is_finish_order(expectid):
    d = r.llen(REDIS_PREFIX.format(expectid))
    return d == 0
    

def set_current_expect(expectid):
    """
    Set current expectid
    """
    r.set(REDIS_PREFIX.format('current_expect'), expectid)
    r.expire(REDIS_PREFIX.format('current_expect'), 100*3600)

def get_current_expect_id():
    """
    Return current expect id 
    """
    return r.get(REDIS_PREFIX.format("current_expect"))


def push_block(expectid=0, blockid=0):
    r.rpush(REDIS_PREFIX.format(expectid), str(blockid))
    r.expire(REDIS_PREFIX.format(expectid), 60 * 1000)


def top_block(expectid=0):
    block_lst = r.lrange(REDIS_PREFIX.format(expectid), 0, -1) or []
    block_lst = sorted(block_lst, reverse=True)
    print(block_lst)
    return  block_lst[0] if block_lst else 0
