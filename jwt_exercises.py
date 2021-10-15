import jwt

token = " eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

decoded = jwt.decode(token, algorithms=["HS256"], options={"verify_signature": False})
print(decoded)
##########################

print(jwt.encode({"username": "mun", "admin": True}, algorithm="HS256", key="", headers={"alg": "none"}))

###############

print(jwt.encode({"username": "admin", "admin": True}, algorithm="HS256", key="secret"))


###########################

public_key = "-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR\nYltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi\ngJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl\nQ4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1\n0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9\nJddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB\n-----END RSA PUBLIC KEY-----\n"
session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6Im11biIsImFkbWluIjpmYWxzZX0.fWrh28GHMcln2CcM59vWRcfosGGTC1BxNR5fXKgLx6s_W40PH3Z9HM1s7fJB9TbmKmwDNLoO2oYF9oQM9u0Zw4CXtMYfedwnZ1yOJIpxhRtY0PyCApTaAzXps2XZKRy8D8dgwvKP1PnLh7cfKKtbnKPzOyQ1Meu6qEK24JcreDET9Lsy7Q_dmHveN2Dv12v0stsRTuYwTFkoR0FxeaeZbYZAde-QAVDqhLIzXYXF3ipPAjJPFIz6xolPNEc1xiZ36xdME3e9q327_GInOz5Wvw6UcqhC7Y-2rIj8NKRYgz2f-k2NSHjCCsfxBX-FrG-dlLPK1YtyP25kIMsP6e1Lgw"

# print(jwt.decode(session, public_key, algorithms=["RS256", "HS256"]))

print(jwt.encode({'username': 'mun', 'admin': True}, algorithm="HS256", key=public_key))

################
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6Im11biIsImFkbWluIjpmYWxzZX0.CTcdtdOiQsq-JOaBZtRHxixrBMyxgrRJnDxmakbaZsj8PwcW9h72Qjl3od2aBDl8dgDHLe-WAm348s5b-dJo1WGuU5xccTBZ649hcpXlm6xOvFxSQNCB3YaXXfnD7jpSyMa4OrsNpmi_hY-fW6k3xEVGz7-s7ZSrCIUlm02-DtHvQJ75IO8xa8C9N6kp1MD6chbFdSFfMNrQw2oRI4oWBqUPuhUURc9DUBewOwbotgXNzZUnbnRLQx-VLkXMg1bboYicL4TkI7qyXTFAKY95JYfrnUKwjial3VbZa7IE3eTx8xelh2AtZjYoGVHO4NdXxdFWUWmbUhvBgdw2mDUvGg"

decoded = jwt.decode(token, algorithms=["RS256"], options={"verify_signature": False})
print(decoded)
