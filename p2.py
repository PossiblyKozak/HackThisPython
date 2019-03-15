import pyperclip
Ans = []
for i in input().split(","):
    if i != " ":
        Ans.append(chr(126 - int(i)).lower())
    else:
        Ans.append(i)
pyperclip.copy(''.join(Ans))