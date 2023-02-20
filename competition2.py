import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
f = open("encoded.txt", "w")
f.write(r.text)
f.close()

code = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

text = ""

f = open("encoded.txt", "r")
for line in f:
    # print(line)
    idx = 0
    for c in line:
        if c in vowels:
            idx += 1
    text += code[idx]
print(text)
