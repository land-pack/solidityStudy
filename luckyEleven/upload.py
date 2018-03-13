import redis
from web3 import Web3, HTTPProvider, IPCProvider


#web3 = Web3(HTTPProvider('http://localhost:8545'))
#web3 = Web3(HTTPProvider('http://192.168.12.34:8545'))
web3 = Web3(HTTPProvider('http://192.168.12.34:9585'))


print(web3.eth.blockNumber)

