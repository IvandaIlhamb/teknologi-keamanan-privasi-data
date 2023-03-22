def enkripsi_text(plaintext,shift):
    hasil = " "

    for i in range(len(plaintext)):
        huruf = plaintext[i]
        
        if huruf==" ":
            hasil+=" "
        # Untuk memeriksa karakter huruf besar kemudian melakukan enkripsi
        elif (huruf.isupper()):
            hasil += chr((ord(huruf) + shift-65) % 26 + 65)

        # Untuk memeriksa karakter huruf kecil kemudian melakukan enkripsi
        else:
            hasil += chr((ord(huruf) + shift-97) % 26 + 97)
    
    return hasil

plaintext = input("Masukkan Teks : ")
#NIM 199
shift = 9
print("Plain Text : " + plaintext)
print("Shift : " + str(shift))
print("Enkripsi Teks : " + enkripsi_text(plaintext,shift))
