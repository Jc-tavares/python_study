import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('#' * 60)
        print('Verificando o ip: ',ip)
        os.system('ping -n 2 {} '.format(ip))
        time.sleep(5)
        #print(ip)
print('#' * 60)