#from pysol.wallet import create_account
from pysol.watch import watching
#from pysol.rpc import get_balance



# Test model
from model.order import Luckyeleven


if __name__ == '__main__':
    #print("Test create_account(12345) == {}".format(create_account('12345')))
    #watching()
    #while(1):
    #    pass
    #print(get_balance())

    with Luckyeleven() as db:
        db.update_succ('0xde1ce69f800cab6451f1e50aeb4c6b088a8f106533e4b121c719f208b4e0bb27')
