import time

def printsystem():
  print('''--------------------
 Console de acesso 
--------------------
''')


documentos = {'file 1': 'arquivo.jpeg', 'file 2': 'arquivo.txt'}
time.sleep(1)
def files():
  file1 = 'Documentos'
  file2 = 'imagens'
  file3 = 'Videos'
  print('Selecione um diretorio:\n')
  time.sleep(0.5)
  print(f'[1]{file1}')
  time.sleep(0.2)
  print(f'[2]{file2}')
  time.sleep(0.2)
  print(f'[3]{file3}')
  time.sleep(0.2)
  selectDir()


def selectDir():
  sDir = input('Insira um numero: ', )
  sDir = int(sDir)
  aDir(sDir)

  
def aDir(diret):
  fi1 = 'Este diretorio é meramente ilustrativa, apenas ignore.'
  fi2 = 'https://imgur.com/gallery/E0IaFd3'
  fi3 = 'https://imgur.com/gallery/lyRmv5X'
  if diret == 1:
    print(fi1)
  elif diret == 2:
    print(fi2)
  elif diret == 3:
    print(fi3)
  else:
    print('não foi possivel acessar o diretorio')
    selectDir()
  time.sleep(3)
  print('deseja continuar o sua navegação ? (s/n)')
  SIMouNAO()


def SIMouNAO():
   SoN = input()
   if SoN == 's':
     files()
   elif SoN == 'n':
     exit()
   else:
     print('Porfavor, digite "s" ou "n"') 
     SIMouNAO()

