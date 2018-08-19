import csv
""" 
cut -f 1  highttemp.txt > col1.txt
cut -f 2 highttemp.txt > col2.txt
"""
with open("hightemp.txt", encoding="utf-8") as f:
    tsv = csv.reader(f, delimiter="\t")
    with open("col1.txt", "w+", encoding="utf-8", newline="") as col1:
        with open("col2.txt", "w+", encoding="utf-8", newline="") as col2:
            col1_writer = csv.writer(col1, delimiter="\t")
            col2_writer = csv.writer(col2, delimiter="\t")
            for s in tsv:
                col1_writer.writerow([s[0]])
                col2_writer.writerow([s[1]])