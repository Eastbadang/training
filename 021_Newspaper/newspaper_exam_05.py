# pip install konlpy

from collections import Counter
from konlpy.tag import Okt


okt = Okt()

words = []
for a in articles:
    words += okt.nouns(a["title"])
    words += okt.nouns(a["content"])

print(Counter(words).most_common())
print(Counter([w for w in words if len(w) > 1]).most_common())