"""
 cut -f 1 hightemp.txt  | sort | uniq -c | sort -n -r
"""
with open("hightemp.txt", encoding="utf-8") as f:
    import csv
    from operator import itemgetter
    prefectures = {}
    for record in sorted(csv.reader(f, delimiter="\t"), key = itemgetter(2), reverse=True):
        prefecture = record[0]
        if prefecture not in prefectures:
            prefectures[prefecture] = 0
        prefectures[prefecture] +=1
    from operator import itemgetter
    for k,v in sorted(prefectures.items(), key=itemgetter(1), reverse=True):
        print(v,k)
