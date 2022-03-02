from sys import stdout
import time
#---------------------------------------------------------------------------
def anim(text):
    words = f"\n{str(text)}\n"
    for char in words:
        time.sleep(0.1)
        stdout.write(char)
        stdout.flush()