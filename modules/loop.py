file = open("data.txt", "r")
for line in file.readlines():
    print(line)
file.close()