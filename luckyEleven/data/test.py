import redis
from web3 import Web3, HTTPProvider, IPCProvider
from abi import abi

#web3 = Web3(HTTPProvider('http://localhost:8545'))
#web3 = Web3(HTTPProvider('http://192.168.12.34:8545'))
w3 = Web3(HTTPProvider('http://192.168.12.34:9585'))
addr = '0x9548bd8b13ceff478f16d206a4752f23579d7ac6'

contract = w3.eth.contract(abi=abi, address=addr)

#print(dir(contract))

#contract.placeOrder('Nihao', transact={'from': w3.eth.accounts[0]})

#print(w3.eth.blockNumber)
#print(contract)


def unlock(w3):
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase='123456')
    return True


print(unlock(w3))
