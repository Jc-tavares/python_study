def change_files(filename, crytoFn, block_size=16):
    
    # modo r de leitura e b de escrita binaria
    with open(filename, 'r+b') as _file:
        # raw value e o valor original do arquivo
        
        raw_value = _file.read(block_size)
            while raw_value:
                cipher_value = crytoFn(raw_value)
                # compara o tamanho do bloco cifrado e plano (plain text)
                if len(raw_value) != len(cipher_value):
                    raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}'.format(len(cipher_value), len(raw_value)))
               
               
               _file.seek(- len(raw_value), 1)
               _file.write(cipher_value)
               
               # le o proximo bloco para encriptar se nao tiver mais blocos ele sai do loop
               
               raw_value = file.read(block_size)
                