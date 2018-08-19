import json
import gzip
import re
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    pattern = re.compile(r"^\[\[Category:(.*)\]\]$")
    for article in map(json.loads, f.readlines()):
        if article["title"] == "イギリス":
            for line in article["text"].split("\n"):
                matcher = pattern.match(line)
                if matcher is not None:
                    print(matcher.group(1))
