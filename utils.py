def toBin(num):
    binString = ''
    while(num > 0):
        remainder = num % 2
        num //= 2
        binString = f'{remainder}' + binString

    #padding
    padString = ''
    for i in range((8 - len(binString))):
        padString += '0'

    return padString + binString