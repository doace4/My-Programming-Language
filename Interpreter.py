with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

count = 0

while count < len(read):
    code = read[count]

    if read[count].__contains__("print"):
        result = globals()[code.split(": ")[1]]
        print(result)

    elif read[count].__contains__("set"):
        code = code.replace("set ", "")
        code = code.split(": ")

        try:
            globals()[code[0]] = int(code[1])

        except ValueError:
            globals()[code[0]] = code[1]

    elif read[count].__contains__("inc"):
        code = code.split(": ")
        globals()[code[1]] += 1

    elif read[count].__contains__("condition"):
        code = code.split(": ")

        if eval(code[1]):
            count += 1

    count += 1
