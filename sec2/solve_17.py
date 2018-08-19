"""
cut -f 1 hightemp.txt | sort | uniq
"""
with open("hightemp.txt", encoding="utf-8") as f:
    import csv
    rows = csv.reader(f, delimiter = "\t")
    prefectures = set()
    for row in rows:
        if row[0] not in prefectures:
            print(row[0])
        prefectures.add(row[0])
