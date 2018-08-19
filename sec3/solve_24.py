import json
import gzip
import re
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    pattern = re.compile(r"(?:File|ファイル):(.+?)\|", re.VERBOSE)
    for article in map(json.loads, f.readlines()):
        if article["title"] == "イギリス":
            search = pattern.findall(article["text"])
            for v in search:
                print(v)
