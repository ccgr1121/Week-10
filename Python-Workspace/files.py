my_file = open(file="filey.txt", mode="w")
my_file.write ("Hello\n")
my_file.write ("\"friends\"")
my_file.close()

my_read = open(file="filey.txt", mode="r")
text = my_read.readline()
while (text != ""):
    print(text)
    text = my_read.readline()
my_read.seek(0)
print(my_read.readline())
my_file.close()