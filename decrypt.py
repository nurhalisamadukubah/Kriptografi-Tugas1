ciphertext = input("Masukkan Ciphertext yang ingin didekripsi : ")
key = 0x61
plaintext= ""

for c in ciphertext:
    plaintext += chr(ord(c)^key)
print("Hasil Dekripsinya adalah : ", plaintext)
plaintext
