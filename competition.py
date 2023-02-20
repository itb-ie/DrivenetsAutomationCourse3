import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
print(r.text)
exit(1)
code = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

text = ""
for line in r.text.split("\n"):
    # print(line)
    idx = 0
    for c in line:
        if c in vowels:
            idx += 1
    text += code[idx]
print(text)
