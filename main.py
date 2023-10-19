from web3 import Web3
import dotenv as _dotenv
import os as os
import utils
from datetime import datetime
import json

rpc = os.environ["ETHEREUM"]
web3 = Web3(Web3.HTTPProvider(rpc))

# Documentation
# https://web3py.readthedocs.io/en/v5/

# Connection to the blockchain
# Allows you to read information about the blockchain, like the blocks and the transactions, create transactions, and interact with smart contracts
if web3.isConnected() == True:
    print('Logged in')
else:
    print('Not logged')

# # Number of the last block in the blockchain
lastBlockNumber = web3.eth.blockNumber
print("Last block number")
print(lastBlockNumber)
print()

# # information of last block
# print('Information of last block')
# blockInformation = web3.eth.getBlock(lastBlockNumber)
# print(blockInformation)
# print()

# # Base fee last block
baseFeePerGas = web3.eth.getBlock(lastBlockNumber)['baseFeePerGas']/(10**9)
print("Base Gas Fee in Gwei: ", "{:,.2f}".format(baseFeePerGas))
print()

# # # Time stamp
timeStamp = web3.eth.getBlock(lastBlockNumber)['timestamp']
print(timeStamp)
print("Date time: ", datetime.fromtimestamp(timeStamp))
print()

# # # Eth balance from a wallet
# wallet = '0x57757E3D981446D585Af0D9Ae4d7DF6D64647806'
# balance = web3.eth.get_balance(wallet)
# print("Wallet balance in ETH")
# print(balance)
# eth_wallet = web3.fromWei(balance, 'ether')
# eth_wallet_in_usd = eth_wallet * 1564
# print(eth_wallet)
# print(eth_wallet_in_usd)
# print()

path = '../utils/'
with open('contrato.json', 'r') as f:
  abi = json.load(f)

# # # Analysis of a contract
tokenAddress = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
tokenContract = web3.eth.contract(address = tokenAddress, abi = abi)

# # # Protocol name
tokenName = tokenContract.functions.name().call()
print("Name: ", tokenName)

# # # # Token Symbol
tokenSymbol = tokenContract.functions.symbol().call()
print("Symbol: ", tokenSymbol)

# # # Token Decimals
tokenDecimals = tokenContract.functions.decimals().call()
print("Decimals: ", tokenDecimals)

# # Total Supply
tokenSupply = tokenContract.functions.totalSupply().call()/(10**tokenDecimals)
print("Supply: ", "{:,.0f}".format(tokenSupply))

# # Wallet balance of the token
walletBalance = tokenContract.functions.balanceOf('0x57757E3D981446D585Af0D9Ae4d7DF6D64647806').call()
print(walletBalance)
print("Token balance in Wallet: ", walletBalance/(10**tokenDecimals))
print()

# # https://etherscan.io
# # https://etherscan.io/chart/ens-register
# # https://dune.com/datactuary/Ethereum
# # https://etherscan.io/chart/active-address
# # https://etherscan.io/chart/address