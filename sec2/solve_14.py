N = int(input())
"""
head -n N hightemp.txt
"""
with open("hightemp.txt", encoding="utf-8") as f :
    for i in f.readlines()[:N]:
        print(i.strip())