publish_channel = 'MyTest'

# Your Node IP/PORT
host_address = 'http://192.168.12.34:9585'

# Configuration yourself contract address
contract_address =  '0xa429da9fc022b96c0754e0d23cf61fb0a213432b'

# Your ABI configration
abi = """
[
    {
      "constant": false,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        }
      ],
      "name": "settleOrder",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "searchBalance",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        }
      ],
      "name": "search",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getNowTime",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        }
      ],
      "name": "getWinNumbers",
      "outputs": [
        {
          "name": "",
          "type": "uint8[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        },
        {
          "name": "randomStr",
          "type": "string"
        }
      ],
      "name": "setWinNumbers",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        },
        {
          "name": "betnums",
          "type": "uint8[]"
        }
      ],
      "name": "placeOrder",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        }
      ],
      "name": "searchOrder",
      "outputs": [
        {
          "components": [
            {
              "name": "orderstatus",
              "type": "uint8"
            },
            {
              "name": "betnums",
              "type": "uint8[]"
            },
            {
              "name": "times",
              "type": "uint8"
            },
            {
              "name": "coins",
              "type": "uint256"
            },
            {
              "name": "prizes",
              "type": "uint256"
            },
            {
              "name": "sender",
              "type": "address"
            }
          ],
          "name": "",
          "type": "tuple"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_issue",
          "type": "string"
        }
      ],
      "name": "settlePrize",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "betcoins",
          "type": "uint256"
        },
        {
          "name": "winNumberCount",
          "type": "uint8"
        }
      ],
      "name": "calculatePrize",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "randomStr",
          "type": "string"
        },
        {
          "name": "numberCount",
          "type": "uint256"
        },
        {
          "name": "numberCountMax",
          "type": "uint256"
        }
      ],
      "name": "generateWinNumbers",
      "outputs": [
        {
          "name": "",
          "type": "bytes"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "msg",
          "type": "address"
        },
        {
          "indexed": false,
          "name": "betnums",
          "type": "uint8[]"
        },
        {
          "indexed": false,
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "placeorder",
      "type": "event"
    }
  ]
"""
