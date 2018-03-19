from model.order import Luckyeleven

from utils.cache import push_block
from utils.cache import get_current_expect_id
from utils.cache import is_finish_order
from utils.cache import is_current_time_over
from pysol.rpc import submit_block_hash


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

    """
    Cache all blockid with key which is expect id
    and after all order finish will can easily get
    the large one
    """
    current_expect_id =  get_current_expect_id()
    push_block(current_expect_id, blockNumber)
    
    p_num =  submit_block_hash()
    print("Prize number is ===>{}".format(p_num))
    
    
    if is_finish_order(current_expect_id) and is_current_time_over(current_expect_id):
        """
        If current expect has finish all order!
        and we can open prize
        """
        p_num =  submit_block_hash()
        print("Prize number is ===>{}".format(p_num))
