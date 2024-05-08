from web3 import Web3,EthereumTesterProvider

print('\nSend ETH--------------------------------------------------')
#w3 = Web3(EthereumTesterProvider)
ALCHEMY_SEPOLIA_URL = 'https://rpc.sepolia.org'
# 连接Sepolia测试网
provider_test = Web3.HTTPProvider(ALCHEMY_SEPOLIA_URL)
w3 = Web3(provider_test)

#w3.is_connected()
#w3.eth.get_block('latest')
account1 = w3.eth.account.from_key("0xf2ef4309ef5492c40547d6a004e119b0a1e7f0a759426ca9d025a02136cb6edd")
account2 = w3.eth.account.from_key("0x60ce73c73a8e58cf9607d3ac154e59c2df6372b864e281bf5ac4543799afa413")
print(account1.address) #0xb601a82e241d9054B4Ad2362b1941FAA30Dd6084
print(account2.address) #0xFd6561a2c87A5b1aa781e067B9779778fE199135
print(f'account1 private key={w3.to_hex(account1.key)}')
print(f'account2 private key={w3.to_hex(account2.key)}')


balance_main = w3.eth.get_balance(account1.address)
print("ETH Balance of account1",w3.from_wei(balance_main,'ether'))
print(w3.eth.get_transaction_count(account1.address))
print(w3.eth.get_transaction_count(account2.address))
#发送ETH，该语法只对测试场景有效（即使用EthereumTesterProvider的场景），在测试账户中，签名过程会被自动完成。
tx_hash = w3.eth.send_transaction({
    "from": account1,
    "to": account2,
    "value": 0.1
})
'''
在正式场景中发送交易，我们还需要补充签名的过程：
# 1. Build a new tx
transaction = {
    'from': acct2.address,
    'to': some_address,
    'value': 1000000000,
    'nonce': w3.eth.get_transaction_count(acct2.address),
    'gas': 200000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
}
# 2. Sign tx with a private key
signed = w3.eth.account.sign_transaction(transaction, private_key)
# 3. Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
tx = w3.eth.get_transaction(tx_hash)
assert tx["from"] == acct2.address
'''