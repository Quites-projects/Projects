from sys import stdout
import time
#---------------------------------------------------------------------------
def anim(text):
    words = f"\n{str(text)}\n"
    for char in words:
        time.sleep(0.1) # mude o tempo de acordo com a sua preferencia
        stdout.write(char)
        stdout.flush()

#use anim("escreva o texto aqui")