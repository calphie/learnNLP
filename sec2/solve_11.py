""" cat highttemp.txt | tr s/\t/ /g """
with open("hightemp.txt", encoding="utf-8") as f:
    print(f.read().replace("\t", " "))