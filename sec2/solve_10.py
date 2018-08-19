"""cat highttemp.txt"""
with open("hightemp.txt", encoding="utf-8") as f:
    print(len(f.readlines()))