s = "https://google.com and then there could be https://yahoo.com or even a website like https://bbc.co.uk"
start = 0
while True:
    start = s.find("https://", start)
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end
