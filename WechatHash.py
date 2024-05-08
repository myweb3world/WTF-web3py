import hashlib

# 定义要哈希的字符串
input_string = "HiCRYang"

# 使用 Keccak-256 哈希算法
hashed = hashlib.sha3_256(input_string.encode()).hexdigest()

# 打印结果
print("HiCRYang 的 Keccak-256 哈希是:", hashed)
