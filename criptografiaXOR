# Criptografando a mensagem
chave = input("Digite a chave: ")

msg = input("Digite a mensagem que você quer que seja criptografada: ")
tam = len(msg)
msg2 = ""
for i in range(tam):
    cript_msg = ord(msg[i])
    cript_chave = ord(chave[i % len(chave)])
    msg_c = chr(cript_msg ^ cript_chave)
    msg2 += msg_c

print("MENSAGEM CRIPTOGRAFADA:")
print(msg2)

# Descriptografando a mensagem

chave = input("Digite a chave para descriptografar a mensagem acima: ")
tam = len(msg2)
msgfinal = ""
for i in range(tam):
    cript_msg = ord(msg2[i])
    cript_chave = ord(chave[i % len(chave)])
    msg_c =chr(cript_msg ^ cript_chave)
    msgfinal += msg_c

print("MENSAGEM DESCRIPTOGRAFADA:")
print(msgfinal)
