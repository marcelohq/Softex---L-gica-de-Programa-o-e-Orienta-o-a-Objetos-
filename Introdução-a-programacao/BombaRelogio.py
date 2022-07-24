import os
import time
def limparTela():
    os.system('cls')

for i in range(10, 0, -1):
    print("Tempo para a explosão: ",i)
    time.sleep(1)
    limparTela()
print("BUM!")

