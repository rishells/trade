f = open("raw_json.txt", "a")
for i in range(0,100):
    f.write(f"{i} - hello saving into file\n")
f.close()