
import redis


from config.basic import redis_host
from config.basic import REDIS_PREFIX


r = redis.Redis(redis_host)



def push_block(expectid=0, blockid=0):
    r.rpush(REDIS_PREFIX.format(expectid), str(blockid))
    r.expire(REDIS_PREFIX.format(expectid), 60 * 1000)


def top_block(expectid=0):
    block_lst = r.lrange(REDIS_PREFIX.format(expectid), 0, -1) or []
    block_lst = sorted(block_lst, reverse=True)
    print(block_lst)
    return  block_lst[0] if block_lst else 0
