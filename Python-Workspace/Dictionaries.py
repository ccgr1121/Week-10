def greeting():
    print("Hello")

obj = {"greet-me": greeting, "Raf": "Boy genius"}
obj["James"] = "Ginger Boy"
obj["Doug"] = "Missing and Ill"
print(obj["Raf"])
chris = {"Role": "Trainer", "Salary": "Too smol", "Holiday": "Bleak"}
obj["chris"]=chris
obj["greet-me"]()
print(obj)