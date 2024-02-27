import base64
import pwn
import re
from Crypto.Util.number import long_to_bytes
from typing import Tuple

# bytes.fromhex() :: str (hex) -> bytes
# base64.b64encode() :: any -> bytes

# Base64: string that encodes 6 bits 

# intro/enc3
# hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# base64 = base64.b64encode(bytes.fromhex(hex))

def xor_encrypt(msg: str, key: int|str) -> str:
    if isinstance(key, str):
        b_key = key.encode('ascii')
    b_key = key
    return pwn.xor(msg.encode('ascii'), b_key).hex()

def xor_bytedecode(hex: str, clue="crypto{FLAG}") -> Tuple[str, int]:
    pattern = re.escape(clue).replace('FLAG', r'(.+)')
    ciphertext = bytes.fromhex(hex)

    for key in range(256):
        try:
            decrypted = pwn.xor(ciphertext, key).decode('ascii')
            if re.search(pattern, decrypted):
                return decrypted, key
        except UnicodeDecodeError:
            pass

    return "", 0

def xor_keydecode(hex_msg: str, key: str) -> str:
    ciphertext = bytes.fromhex(hex_msg)
    key_hex = list(map(ord, key))

    msg = ""
    for (i, c) in enumerate(ciphertext):
        msg += chr(c ^ key_hex[i%len(key_hex)])

    return msg

def gcd(a: int, b: int) -> int:
    m = max(a, b) // 2
    ret = 1
    i = 2
    while i <= m:
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            print(i)
            ret *= i
        else:
            i += 1
    return ret

def test_1():
    msg = ("crypto{myXORkey}", 16)
    assert msg == xor_bytedecode(xor_encrypt(*msg))
