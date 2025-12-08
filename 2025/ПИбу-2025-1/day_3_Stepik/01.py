lst = [
    "топот", 
    "топор", 
    "Поп", 
    "Аргентина манит негра",
    "А роза упала на лапу Азора!",
    "Да, искать такси - ад.",
    12321,
    123456789
]

str_ = ' !.,:;-'

for s in lst:
    tmp = str(s).lower()
    t = ''
    for smb in tmp:
        if smb not in str_:
            t += smb
    print(s, t, t == t[::-1])