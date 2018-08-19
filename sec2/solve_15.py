"""
tail -n N hightemp.txt
"""

N = int(input())
with open("hightemp.txt", encoding="utf-8") as f :
    for i in f.readlines()[-N:]:
        print(i.strip())