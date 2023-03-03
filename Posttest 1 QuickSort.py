import os
os.system("cls")
import random 

angka = random.sample(range(1, 100), 10)
def quickSort(angka):
    if len(angka) <= 1:
        return angka
    else:
        pivot = angka[0]
        kiri = [x for x in angka[1:] if x <= pivot]
        kanan= [x for x in angka[1:] if x >= pivot]
        return quickSort(kiri) + [pivot] + quickSort(kanan)

print("=========================QuickSort=========================")
print("============================^.^============================")
print("sebelum Diurutkan =" ,angka) 
hasil = quickSort(angka)
print("============================^.^============================")
print("setelah Diurutkan =" , hasil)