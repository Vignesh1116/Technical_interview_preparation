# Count character frequency

string = input("Enter a string: ")

for ch in string:
    print(ch, ":", string.count(ch))