# ASCII
bytes = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("".join(map(lambda x: chr(x), bytes)))

# Hex
hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(str(bytearray.fromhex(hex), "ASCII"))

# Base64
import base64
hex2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(str(base64.b64encode(bytearray.fromhex(hex2)), "ASCII"))

# Bytes and Big Integers
from Crypto.Util.number import long_to_bytes
integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(str(long_to_bytes(integer), "ASCII"))

# Challenge -> pwntools_example.py

###

# XOR Starter
print("".join([chr(x) for x in [ord(char) ^ 13 for char in "label"]]))

# XOR Properties
from pwn import xor

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_xor_key2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_xor_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_all = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(bytearray.fromhex(key1), bytearray.fromhex(key1_xor_key2))
key3 = xor(key2, bytearray.fromhex(key2_xor_key3))
flag = xor(bytearray.fromhex(key1), key2, key3, bytearray.fromhex(flag_xor_all))
print(flag.decode("ASCII"))

# Favourite Byte
for byte in range(128):
    output = str(xor(bytearray.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"), byte), "ASCII")
    if output.startswith("crypto"):
        print(output)

# You either know, XOR you don't
hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
print(xor(bytearray.fromhex(hex)[:7], b"crypto{")) # myXORke
print(xor(bytearray.fromhex(hex), b"myXORkey"))

# Lemur XOR
from PIL import Image

lemur = Image.open("./general/lemur.png")
flag = Image.open("./general/flag.png")

width, height = lemur.size
lemur = lemur.load()
flag = flag.load()

result = Image.new("RGB", (width, height))
result_pixels = result.load()

for i in range(width):
    for j in range(height):
        red1, green1, blue1 = lemur[i, j]
        red2, green2, blue2 = flag[i, j]

        red = red1 ^ red2
        green = green1 ^ green2
        blue = blue1 ^ blue2

        result_pixels[i, j] = (red, green, blue)

result.save("/general/lemur_xor_flag.png")

#

