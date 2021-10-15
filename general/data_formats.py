# noinspection PyPackageRequirements
import Crypto.PublicKey.RSA

with open("privacy_enhanced_mail.pem") as f:
    key = Crypto.PublicKey.RSA.import_key(f.read())
    print(key.d)

with open("2048-rsa-example-cert.der", "r+b") as f:
    key = Crypto.PublicKey.RSA.import_key(f.read())
    print(key.n)

with open("bruce_rsa.pub") as f:
    key = Crypto.PublicKey.RSA.import_key(f.read())
    print(key.n)

with open("transparency.pem") as f:
    key = Crypto.PublicKey.RSA.import_key(f.read())
    print(key.n)
