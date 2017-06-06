textToWrite = "Hello, this text should be written in a file"

# 'w' for 'write, 'r' for 'read'
# 'with' makes sure, the file is closed properly after block, or in case of a crash.
# writing a file will create the file if it does not exit

with open('example.txt','w') as f:
    f.write(textToWrite)

with open('example.txt','r') as f:
    readText = f.read()

print readText
