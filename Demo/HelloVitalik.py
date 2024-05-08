from web3 import Web3

#1
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
print(w3.is_connected())  #True
print(w3.eth.get_balance("vitalik.eth")) #605370759607649911133

#2
# 利用公共rpc节点连接以太坊网络
# 可以在 https://chainlist.org 上找到
ALCHEMY_MAINNET_URL = 'https://rpc.ankr.com/eth'
#ALCHEMY_SEPOLIA_URL = 'https://rpc.sepolia.org'
# 连接以太坊主网
provider_main = Web3.HTTPProvider(ALCHEMY_MAINNET_URL)
# 连接Sepolia测试网
#provider_test = Web3.HTTPProvider(ALCHEMY_SEPOLIA_URL)
w3_main = Web3(provider_main)
#w3_test = Web3(provider_test)
# 1. 查询vitalik在主网和Sepolia测试网的ETH余额
print("1. 查询vitalik在主网和Sepolia测试网的ETH余额")
balance_main = w3_main.eth.get_balance("vitalik.eth")
#balance_test = w3_test.eth.get_balance("vitalik.eth")
# 将余额输出在console（主网）
# 使用Web3.from_wei()函数将返回的结果转化为ETH单位：
print("ETH Balance of vitalik",w3_main.from_wei(balance_main,'ether')) #605.370759607649911133
# 输出Sepolia测试网ETH余额
#print("Sepolia ETH Balance of vitalik",w3_test.from_wei(balance_test,'ether'))

# 2. 查询provider连接到了哪条链
print("2. 查询provider连接到了哪条链")
chain_id_main = w3_main.eth.chain_id
print(f"Chain id: {chain_id_main}")
# 3. 查询区块高度
print("3. 查询区块高度")
block_number_main = w3_main.eth.block_number
print(f"Block number: {block_number_main}")
# 6. 查询区块信息
print("3.1. 查询区块信息")
block_main = w3_main.eth.get_block(0)
print(block_main)
# 4. 查询 vitalik 钱包历史交易次数
print("4. 查询 vitalik 钱包历史交易次数")
tx_count_main = w3_main.eth.get_transaction_count("vitalik.eth")
print(f"Tx Count: {tx_count_main}")
# 5. 查询当前建议的gas设置
print("5. 查询当前建议的gas设置")
fee_data_main = w3_main.eth.gas_price
print(f"Gas price: {w3_main.from_wei(fee_data_main, 'gwei')}")
# 7. 给定合约地址查询合约bytecode，例子用的WETH地址
print("7. 给定合约地址查询合约bytecode，例子用的WETH地址")
weth_address = w3_main.to_checksum_address("0xc778417e063141139fce010982780140aa0cd5ab")
code_main = w3_main.eth.get_code(weth_address)
print(code_main.hex())