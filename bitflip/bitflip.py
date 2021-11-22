from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad,unpad
from time import sleep
from secret import flag,key
from os import urandom


def encryption_oracle(pt,iv,key):
	return (AES.new(key,AES.MODE_CBC,iv)).encrypt(pad(pt.encode(),16))

def decryption_oracle(ct,iv,key):
    return (unpad((AES.new(key,AES.MODE_CBC,iv)).decrypt(ct),16))

if __name__ == "__main__":
    print("Hey junior!!! flip the bits...get the flag....!!!")
    sleep(1)
    iv =  b"secret_sentences" 
    cookie = "admin=no!"
    ct = encryption_oracle(cookie,iv,key)
    pt = decryption_oracle(ct,iv,key)
    if b"admin=yes" in pt:
        print(flag)
    else:
        print("Try to get the flag!!!")

