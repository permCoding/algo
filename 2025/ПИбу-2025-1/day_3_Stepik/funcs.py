def dec_to(n, base=2):
    if n == 0: return 0
    
    res = ''
    while n > 0:
        res += str(n % base)
        n //= base
    
    return res[::-1]

# написать функцию перевода из двоичного в десятичное
def bin_to_dec(b):  # b - string
    dec = 0
    #
    #
    #
    return dec
