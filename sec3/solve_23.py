import json
import gzip
import re

with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    pattern = re.compile(r"^(==+)(.*)\1$")
    for article in map(json.loads, f.readlines()):
        if article["title"] == "イギリス":
            for line in article["text"].split("\n"):
                matcher = pattern.match(line)
                if pattern.match(line) is not None:
                    section_level = len(matcher.group(1))
                    print("\t" * (section_level - 2), matcher.group(3), section_level - 1)
