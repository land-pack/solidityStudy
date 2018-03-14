import redis
import json
from web3 import Web3, HTTPProvider, IPCProvider, RPCProvider
from web3.contract import ConciseContract

from pysol.abi import abi as abi_conf
abi_conf = json.loads(abi_conf)

w3 = Web3(HTTPProvider('http://192.168.12.34:9585'))
addr = '0x9548bd8b13ceff478f16d206a4752f23579d7ac6'


contract = w3.eth.contract(abi=abi_conf, address=addr)


def unlock(w3):
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase='123456')
    return True
unlock(w3)

print("Current accounts={}".format(w3.eth.accounts[0]))

def place(addr=w3.eth.accounts[0], value=0, expectid='1803141010', number=[0,1,2,3,4], gas=40000000 ):
    """
    user address
    @param value    : float :   0.00021
    @param expectid : int   :   1803150810
    @param number   : list  :   [1,2,3,4,5]
    @param gas      : int   :   4000000
    """
    print("Origin number={} | type of number={}".format(number, type(number)))
    number = [int(i) for i in number]
    value = float(value)
    print("addr={} | value={} | expectid={} | number={} | gas={}".format(addr, value, expectid, number, gas))   
    value = 2
    ret = contract.transact(
            {   'from': addr, 
                'gas': gas, 
                'value': value
            }).placeOrder(
            expectid, 
            number)
    return ret


if __name__ == '__main__':
    pass
