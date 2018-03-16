import redis
import json
from web3 import Web3, HTTPProvider, IPCProvider, RPCProvider
from web3.contract import ConciseContract

from config.basic import host_address
from config.basic import abi as abi_conf
from config.basic import contract_address as addr
from utils.cache import top_block, get_current_expect_id


abi_conf = json.loads(abi_conf)
w3 = Web3(HTTPProvider(host_address))
contract = w3.eth.contract(abi=abi_conf, address=addr)


def unlock(w3):
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase='123456')
    return True


print("Current accounts={}".format(w3.eth.accounts[0]))



def place(addr=w3.eth.accounts[0], value=0, expectid='1803141010', number=[0,1,2,3,4], gas=40000000):
    """
    user address
    @param value    : float :   0.00021
    @param expectid : int   :   1803150810
    @param number   : list  :   [1,2,3,4,5]
    @param gas      : int   :   4000000
    """
    #unlock(w3)
    number = [int(i) for i in number]
    #value = int(value)
    #print("addr={} | value={} | expectid={} | number={} | gas={}".format(addr, value, expectid, number, gas))   
    ret = contract.transact(
            {   'from': addr,
                'gas': gas, 
                'value': w3.toWei(value,"ether")
            }).placeOrder(
            expectid, 
            number)
    return ret


def get_balance(addr=w3.eth.accounts[0]):
    """
    account addr
    """
    return w3.eth.getBalance(addr)

def get_prize_num(expectid=None, addr=w3.eth.accounts[0], gas=400000000):

    print("addr -->{}".format(addr))
    max_block = top_block() or 10385
    if not max_block:
        print("Invalid max_block")
        return 

    print("max_block num={}".format(max_block))
    block_obj = w3.eth.getBlock(max_block)
    print("block_obj={}".format(block_obj))
    block_hash =  block_obj.get("hash")

    print("block_hash={}".format(block_hash))
    exp = expectid if expectid else get_current_expect_id()
    return contract.transact(
            {   'from': addr,
                'gas': gas, 
            }).setWinNumbers(exp, str(block_hash))


def get_number(expectid=0):
    ep=contract.call().getWinNumbers(expectid)
    print(ep)
