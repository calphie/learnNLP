"""
sort -k 3,3 -n -r hightemp.txt
"""
with open("hightemp.txt", encoding="utf-8") as f:
    import csv
    from operator import itemgetter
    for t in sorted(csv.reader(f, delimiter="\t"), key = itemgetter(2), reverse=True):
        print("\t".join(t))

