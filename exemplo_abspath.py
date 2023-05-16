import os
#pegar o diretorio atual do arquivo que foi executado
path = os.getcwd()
print(path)
absolute_path = os.path.abspath(os.path.join(path, 'teste1', 'teste2'))
print(absolute_path)