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

def textTobin(text):
    binary = ''
    for t in text:
        binary += toBin(ord(t))
    return binary

text = input("Enter some text: ")
binary = textTobin(text)

print(binary)