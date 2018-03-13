import redis
import json
from web3 import Web3, HTTPProvider, IPCProvider, RPCProvider
from web3.contract import ConciseContract

from abi import abi as abi_conf
abi_conf = json.loads(abi_conf)

#web3 = Web3(HTTPProvider('http://localhost:8545'))
#web3 = Web3(HTTPProvider('http://192.168.12.34:8545'))
w3 = Web3(HTTPProvider('http://192.168.12.34:9585'))
#w3 = Web3(RPCProvider('http://192.168.12.34:9585'))
addr = '0x9548bd8b13ceff478f16d206a4752f23579d7ac6'

#contract = w3.eth.contract(abi=abi, address=addr)
contract = w3.eth.contract(abi=abi_conf, address=addr)


#tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})
#ontract.transact().placeOrder('1803120252', [1,2,3,4,5], {'from': w3.eth.accounts[0], 'gas': 41000, 'value': 12})
def unlock(w3):
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase='123456')
    return True
unlock(w3)
contract.transact(
{'from': w3.eth.accounts[0], 'gas': 41000, 'value': 12}
).placeOrder('1803120252', [1,2,3,4,5])
#print(help(contract.transact().placeOrder))
print(contract.call().searchBalance())
#print(contract)
#print(help(contract.factory(w3)))

#print(w3.eth.blockNumber)
#print(contract)





unlock(w3)


#contract_instance = w3.eth.contract(
#    address=addr, abi=abi, ContractFactoryClass=ConciseContract)


