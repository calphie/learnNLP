"""
split -n N hightemp.txt
"""
N: int = int(input())
with open("hightemp.txt", encoding="utf-8") as f:
    import csv

    rows = [v for v in csv.reader(f, delimiter="\t")]
    records = len(rows)
    if N > records:
        import sys
        print(N, "is larger than file lines", file=sys.stdout)
        sys.exit(1)
    else:
        import os, os.path, shutil
        path = os.path.join(os.path.curdir, "generated")
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path, exist_ok=False)
        lines_par_file = records // N
        cnt = 0
        for i in range(N):
            if i < records - lines_par_file * N:
                nxt = cnt + lines_par_file + 1
            else:
                nxt = cnt + lines_par_file
            with open(os.path.join(path, "{}.txt".format(i + 1)), "w+", encoding="utf-8", newline="") as output_file:
                writer = csv.writer(output_file, delimiter="\t")
                for v in range(cnt, nxt):
                    writer.writerow(rows[v])
            cnt = nxt
