s = '100 99'
lst = s.split()

print(lst[0] > lst[1])

s = '0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# for smb in s:
#     print(smb, ord(smb))
    
for i in range(48, 48+10):
    print(i, chr(i))