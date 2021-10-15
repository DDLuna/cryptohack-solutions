from pwn import *
import json
import Crypto.Util.number
import codecs

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()
while "flag" not in received:
    encoding = received["type"]
    encoded = received["encoded"]

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode("ASCII")
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode("ASCII")
    elif encoding == "bigint":
        decoded = Crypto.Util.number.long_to_bytes(int(encoded, base=16)).decode("ASCII")
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, "rot13")
    elif encoding == "utf-8":
        decoded = "".join(list(map(lambda x: chr(x), encoded)))
    else:
        raise Exception(f"{encoding} not implemented")

    json_send({"decoded": decoded})
    received = json_recv()
    if "error" in received:
        print("ERROR: ", received)
        break

print(received)
