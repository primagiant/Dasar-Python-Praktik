# Dadu
import random
import os


def rolling():
    dadu = []
    dadu1 = random.randint(1, 6)
    dadu2 = random.randint(1, 6)
    dadu3 = random.randint(1, 6)
    dadu.append(dadu1)
    dadu.append(dadu2)
    dadu.append(dadu3)
    return dadu


while True:
    print(rolling())

    print("Pilih Opsi :")
    print("1.Lagi")
    print("2.Exit")
    opsi = int(input("pilih : "))
    if(opsi == 2):
        break
    os.system('cls')

print("Thankyou")
