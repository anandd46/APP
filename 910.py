# std=["Anand","manu","madhu","viki"]
# with open("std.txt","w") as f:
#     for i in std:
#         f.write(i+"\n")
# print("student names are written successfully in std.txt file")
# print("file close",f.closed)



with open("agecl.png", "rb") as sf:
    with open("op.png", "wb") as df:
        chunkcount = 1
        while chunk := sf.read(4096):
            df.write(chunk)
            print(f"{chunkcount} ({len(chunk)}) chunk copied")
            print(f"Byte preview: {chunk[:50]}")
            print("-" * 40)
            chunkcount += 1
print("\nFile copy completed successfully, total chunks:", chunkcount - 1)
