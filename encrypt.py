plaintext = input("Masukkan Plaintext yang ingin dienkripsi : ")
key = 0x61
ciphertext = ""

for c in plaintext:
    ciphertext += chr(ord(c)^key)
print("Hasil Enkripsinya adalah : ", ciphertext)
ciphertext
