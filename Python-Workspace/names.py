import fileinput

my_file = open(file="names.txt", mode="w")
my_file.write ("James\n")
my_file.write ("Palpy\n")
my_file.write ("Tyler\n")
my_file.close()

for line in fileinput.input("names.txt", inplace = True):
    
    if "Palpy" in line:
        s = "Palpy"
        s += " is the senate"
        print(s)
    else:
        print(line[:-1])

my_read = open(file="names.txt", mode="r")
text = my_read.readline()
while (text != ""):
    print(text)
    text = my_read.readline()
print(my_read.readline())
my_file.close()