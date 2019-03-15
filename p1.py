import pyperclip
x = input().split(', ')
x.sort()
pyperclip.copy(', '.join(x))