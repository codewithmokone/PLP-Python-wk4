# Question 1
# Opening and reading a file
fileOne = open("file.txt") 

fileOneRead = fileOne.read() 

print("First file content: ", fileOneRead)

# Creating, writing file one content to the new file
fileTwo = open("file2.txt", "w")

fileTwo.write(f"{fileOneRead}\nSecond line") 

fileTwo = open("file2.txt")

print("Second file content: ", fileTwo.read())

fileOne.close()
fileTwo.close()

# Question 2
try:
    fileName = input("Please enter a file name: ")
    readFile = open(f"{fileName}", "r")
    print("File content:\n", readFile.read())
except:
    print("File not found.")
finally:
    print("Have a nice day.")