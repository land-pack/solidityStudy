#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#      Filename: wallet.py
#
#        Author:
#   Description: ---
#        Create: 2018-03-13 13:47:17
# Last Modified: 2018-03-13 13:47:17
#   Changes Log:


from web3 import Web3, HTTPProvider

web3 = Web3(HTTPProvider("http://192.168.12.117:8545"))


def create_account(password):
    try:
        return web3.personal.newAccount(password)
    except:
        raise


def import_account(privatekey, keytype, password):
    try:
        if keytype == 'pk':
            return web3.personal.importRawKey(privatekey, password)
        if keytype == 'pw':
            pass
        return ''
    except:
        raise


def withdraw(value, to, password, frm=None):
    """
    @brief: 从from向to转账value
    """
    #当frm为none，默认为defaultAccount
    if frm is None:
        frm = web3.eth.coinbase

    #解锁账户
    try:
        unlock = web3.personal.unlockAccount(frm, password)
        if not unlock:
            raise Exception("Unlock account faild！ Wrong password")
    except:
        raise

    #发送交易
    transaction = {
        'from': frm,
        'to': to,
        'value': value
    }
    try:
        txhash = web3.eth.sendTransaction(transaction)
        return txhash
    except:
        raise
