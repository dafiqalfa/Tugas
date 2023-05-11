text = 'The Fox and fox.'
oldText = 'fox' 
newText = 'dog'

for i in text:
    x = i.replace(oldText, newText)
    print(x, end='')