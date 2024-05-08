# This code will loop through the data.txt file and print each line until the end of the file and then close the file
def loop():
    file = open("data.txt", "r")
    for line in file.readlines():
        print(line)
    file.close()

