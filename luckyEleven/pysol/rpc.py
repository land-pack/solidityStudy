import redis
import json
from web3 import Web3, HTTPProvider, IPCProvider, RPCProvider
from web3.contract import ConciseContract

from pysol.config import host_address
from pysol.config import abi as abi_conf
from pysol.config import contract_address as addr

abi_conf = json.loads(abi_conf)
w3 = Web3(HTTPProvider(host_address))
contract = w3.eth.contract(abi=abi_conf, address=addr)


def unlock(w3):
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase='123456')
    return True


print("Current accounts={}".format(w3.eth.accounts[0]))



def place(addr=w3.eth.accounts[0], value=0, expectid='1803141010', number=[0,1,2,3,4], gas=40000000 ):
    """
    user address
    @param value    : float :   0.00021
    @param expectid : int   :   1803150810
    @param number   : list  :   [1,2,3,4,5]
    @param gas      : int   :   4000000
    """
    unlock(w3)
    number = [int(i) for i in number]
    value = int(value)
    #print("addr={} | value={} | expectid={} | number={} | gas={}".format(addr, value, expectid, number, gas))   
    ret = contract.transact(
            {   'from': addr, 
                'gas': gas, 
                'value': value
            }).placeOrder(
            expectid, 
            number)
    return ret


def get_balance(addr=w3.eth.accounts[0]):
    """
    account addr
    """
    return w3.eth.getBalance(addr)
