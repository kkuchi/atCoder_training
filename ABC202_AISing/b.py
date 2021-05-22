s = input()

out = ""

for char in s[::-1]:
    if char not in ["6", "9"]:
        out += char
        continue
    else:
        if char == "6":
            out += "9"
        elif char == "9":
            out += "6"

print(out)