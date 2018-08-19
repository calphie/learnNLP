import json
import gzip
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for article in map(json.loads, f.readlines()):
        if article["title"] == "イギリス":
            print(article["text"])
