from model.order import Luckyeleven

def transfer_callback(param):
    print(param)
    print(type(param))

    transactionHash = param.get("transactionHash")
    blockNumber = param.get("blockNumber")
    print("transactionHash={} -- {}".format(transactionHash, blockNumber))
    with Luckyeleven() as db:
        db.update_succ(transactionHash, blockNumber)

