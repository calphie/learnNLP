import csv
"""
paste col1.txt col2.txt
"""

with open("col1.txt", encoding="utf-8") as col1:
    with open("col2.txt", encoding="utf-8") as col2:
        with open("merge12.txt", "w", encoding="utf-8", newline="") as write_file:
            col1_reader = csv.reader(col1, delimiter="\t")
            col2_reader = csv.reader(col2, delimiter="\t")
            csv_reader = csv.writer(write_file, delimiter="\t")
            for v,x in zip(col1_reader, col2_reader):
                csv_reader.writerow([v[0], x[0]])
