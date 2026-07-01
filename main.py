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

def header(text):
    mode = '0100'
    count = 0
    for t in text:
        count += 1
    count = toBin(count)
    return mode + count

def body(text):
    data = ''
    for t in text:
        data += toBin(ord(t))
    return data

def stream(text):
    return header(text) + body(text) + "0000"


text = input("Enter some text: ")
final = stream(text)
print(final)