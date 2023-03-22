import string


# Daftar yang berisi semua karakter
data = string.ascii_letters

	
"""
Membuat dictionary untuk menyimpan substitusi
alfabet yang diberikan dalam teks biasa berdasarkan kunci
"""

	
dict = {}
key = 4

for i in range(len(data)):
	dict[data[i]] = data[(i+key)%len(data)]


plain_text= input("Masukkan Teks : ")
cipher_text=[]


for char in plain_text:
	if char in data:
		temp = dict[char]
		cipher_text.append(temp)
	else:
		temp =char
		cipher_text.append(temp)
		
cipher_text= " ".join(cipher_text)
print("Cipher Text : ",cipher_text)

	
"""
Buat kamus untuk menyimpan substitusi
untuk alfabet yang diberikan dalam sandi
teks berdasarkan kunci
"""

	
dict2 = {}	
for i in range(len(data)):
	dict2[data[i]] = data[(i-key)%(len(data))]
	
# Deskripsi Plain Text
decrypt_text = []

for char in cipher_text:
	if char in data:
		temp = dict2[char]
		decrypt_text.append(temp)
	else:
		temp = char
		decrypt_text.append(temp)
		
decrypt_text = " ".join(decrypt_text)
print("Dekripsi plain text :", decrypt_text)
