std=["Anand","manu","madhu","viki"]
with open("std.txt","w") as f:
    for i in std:
        f.write(i+"\n")
print("student names are written successfully in std.txt file")
print("file close",f.closed)