with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

count = 0

while count < len(read):
    code = read[count]

    if "print" in code:
        result = globals()[code.split(": ")[1]]
        print(result)

    elif "set" in code:
        code = code.replace("set ", "")
        code = code.split(": ")

        try:
            globals()[code[0]] = int(code[1])

        except ValueError:
            globals()[code[0]] = code[1]

    elif "inc" in code:
        code = code.split(": ")
        globals()[code[1]] += 1
        
    elif "dec" in code:
        code = code.split(": ")
        globals()[code[1]] -= 1

    elif "condition" in code:
        code = code.split(": ")

        if eval(code[1]):
            count += 1

    count += 1
