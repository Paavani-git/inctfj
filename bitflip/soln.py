from Crypto import Cipher
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from time import sleep
from secret import flag,key
from os import urandom



def encryption_oracle(pt,iv,key):
	return (AES.new(key,AES.MODE_CBC,iv)).encrypt(pad(pt.encode(),16))

def decryption_oracle(ct,iv,key):
    iv = list(iv)    
    iv[8] = iv[8] ^ ord(cookie[8]) ^ ord("s")
    iv[7] = iv[7] ^ ord(cookie[7]) ^ ord("e")
    iv[6] = iv[6] ^ ord(cookie[6]) ^ ord("y")       
    iv = b"".join([bytes([i]) for i in iv])
    return (unpad((AES.new(key,AES.MODE_CBC,iv)).decrypt(ct),16))

if __name__ == "__main__":
    print("Hey junior!!! flip the bits...get the flag....!!!")
    sleep(1)
    cookie = "admin=no!"
    iv =  b"secret_sentences"
    ct = encryption_oracle(cookie,iv,key)
    pt = decryption_oracle(ct,iv,key)
    if b"admin=yes" in pt:
        print(flag)
    else:
        print("Try to get the flag!!!")

