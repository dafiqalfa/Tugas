inputText = str.upper(input("Masukan Text yang akan anda enkripsi, "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lalphabet = (len(alphabet))
linputText = (len(inputText))
key = 4
def enkripsi(): 
    result = ' '
    for i in range(linputText):
        nText = inputText[i]
        if nText in alphabet:
            alphabetenk = alphabet.find(nText)
            alphabetenk += key
            if alphabetenk >= lalphabet:
               alphabetenk %= lalphabet
            nText = alphabet[alphabetenk]
        result += f'{nText}'
    return result

finalresult = enkripsi()
print(finalresult)