print(help("".center))

print("Bogdan".center(50))
print("Bogdan".center(50, "!"))
# print("Bogdan".center(50, "!@#$")) this is an exception!

text = "banana"
print("letter a shows in", text, text.count("a"), "times")
print("substring 'an' shows in", text, text.count("an"), "times")
print("substring 'ana' shows in", text, text.count("ana"), "time(s)")
print("substring 'xx' shows in", text, text.count("xx"), "time(s)")
text = "xx"*4
print("substring 'xx' shows in", text, text.count("xx"), "time(s)")

text = "this is a text!"
print(text.endswith("!"))
print(text.endswith("text!"))
print(text.endswith("text?"))

text = "cat"
print(text.replace("c", "r"))
text = "caaaat"
print(text.replace("a", "e"))
print(text.replace("caaaa", "RA"))
print(text)

text = "this is a nice text to have as an example"
print(text.split())
print(text.split(" "))
print(text.split("is"))

# join
print("----- Join ----")
print(text, text.split())
print("!".join(text.split()))
print("!X!".join(text.split()))
join_value = "@@"
x = join_value.join(["1", "2", "3", "4", "5", "11"])
print(x)

text = "hello"
print(text.__add__("bye"))

text = "cat"
print(text.replace("c", "r"))
text2 = str.replace(text, "c", "r")
print(text2)
print("text stays the same:", text)
