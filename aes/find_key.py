from Crypto.Cipher import AES
import hashlib

ciphertextStr = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
with open("words.txt") as f:
    for word in [w.strip() for w in f.readlines()]:
        key = hashlib.md5(word.encode()).digest()
        ciphertext = bytes.fromhex(ciphertextStr)
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypt = cipher.decrypt(ciphertext)
            plain = decrypt.decode("utf-8")
            print(plain)
        except ValueError:
            continue
