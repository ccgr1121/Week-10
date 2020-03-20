def substring(string, index, size):
    if index + size > len(string):
        return None
    else:
        return string[index:index+size]

string1 = "heiliges römisches reich"
string2 = "sacrum imperium romanum"

strings = [string1, string2]
if len(strings[0])>len(strings[1]):

    strings[0] = string2
    strings[1] = string1

short_string = strings[0]
long_string = strings[1]

for sub_length in range(len(short_string)+1):
    for sub_index in range(len(short_string) + 1 - sub_length):
        test = substring(short_string, sub_index, sub_length)
        print("checking:", test)
        if test in long_string:
            print(test, "is in", long_string)
            longest = test
print("Longest sequence in:", short_string, "&", long_string, "is", longest)