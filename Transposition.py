import math
key=input("KEYWORD : ").lower().replace(" ", "")
plain_text = input("PLAIN TEXT: ").lower().replace(" ", "")

len_key = len(key)
len_plain = len(plain_text)
row = int(math.ceil(len_plain / len_key))
matriks = [ ['X']*len_key for i in range(row) ]



t = 0
for r in range(row):
  for c,ch in enumerate(plain_text[t : t+ len_key]):
    matriks[r][c] = ch
  t += len_key

#Membuat urutan abjad
sort_order = sorted([(ch,i) for i,ch in enumerate(key)])  


cipher_text = ''
for ch,c in sort_order:
  for r in range(row):
    cipher_text += matriks[r][c]
  
print("Encryption")
print("Plain text :",plain_text)
print("Cipher text :",cipher_text)
