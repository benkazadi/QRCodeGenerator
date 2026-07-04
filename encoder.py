from utils import toBin

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