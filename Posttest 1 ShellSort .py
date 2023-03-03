import os
os.system("cls")
from random import randint

def shellsort(listt):
    n=len(listt)
    gep = n // 2
    
    while gep > 0:
        for i in range(gep,n):
            x = listt[i]
            j = i
            
            while j >= gep and listt[j - gep] > x:
                listt[j] = listt[j - gep]
                j -= gep

            listt[j] = x
        gep //= 2

    return listt


angka = []
for i in range(10):
    abc = randint(1,100)
    angka.append(abc)

print("=========================ShellSort=========================")
print("============================^.^============================")
print("sebelum Diurutkan",angka)
hasil = shellsort(angka)
print("============================^.^============================")
print("sesudah Diurutkan", hasil)