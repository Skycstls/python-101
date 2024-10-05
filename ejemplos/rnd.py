from Crypto.Random import random
from Crypto.Random import get_random_bytes
from Crypto.Random import atfork

n0 = random.randint(1, 100)
n1 = random.randint(-100, 100)

b0 = get_random_bytes(8)
b1 = get_random_bytes(16)
b2 = get_random_bytes(32)

print("Valores aleatorios:")
print(n0)
print(n1)
print("-----")
print(b0)
print(b1)
print(hex(int.from_bytes(b2, byteorder='big')))