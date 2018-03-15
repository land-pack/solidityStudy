from model.order import Luckyeleven


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

