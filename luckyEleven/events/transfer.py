from model.order import Luckyeleven

from utils.cache import push_block
from utils.cache import get_current_expect_id


def transfer_callback(param):
    transactionHash = param.get("transactionHash")
    blockNumber = param.get("blockNumber")
    print("transactionHash={} -- {}".format(transactionHash, blockNumber))
    data = {
	    "msg_type": "link",
	    "msg_code": 1005,
	    "data": {
	    	"trade_addr": transactionHash,
	    }
    }
    with Luckyeleven() as db:
        db.update_succ(transactionHash, blockNumber)

    current_expect_id =  get_current_expect_id()
    push_block(current_expect_id, blockNumber)
