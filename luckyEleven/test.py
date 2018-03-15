from pysol.wallet import create_account
from pysol.watch import watching
from pysol.rpc import get_balance



if __name__ == '__main__':
    #print("Test create_account(12345) == {}".format(create_account('12345')))
    #watching()
    print(get_balance())
