dct = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1_000
}

number_Romans = [
    "IIDIIIM",
    "VIII",
    "IV"
]

for number_Roman in number_Romans:
    sm = 0
    for elm in number_Roman:
        sm += dct[elm]
    print(sm)
