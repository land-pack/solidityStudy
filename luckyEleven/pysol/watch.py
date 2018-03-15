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



def transfer_callback():
    print("Got signal")


def watching():

    filter_ = contract.on("placeorder", {})
    print(dir(filter_))
    filter_.watch(transfer_callback)
