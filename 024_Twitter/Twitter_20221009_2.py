# https://livedata.tistory.com/21?category=1026425

from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Twitter
from lxml import html
import pytagcloud  # requires Korean font support
import sys

r = lambda: random.randint(0, 255)
# 글씨의 랜덤색깔
color = lambda: (r(), r(), r())


def get_tags(text, ntags=50, multiplier=3):  # 전에 했던 명사 탐색
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return [{'color': color(), 'tag': n, 'size': (c * multiplier) / 2} \
            for n, c in count.most_common(ntags)]


def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)
# 그림 그리기

def main():
    text_file = open("out_cleand.txt", 'r')
    text = text_file.read()
    tags = get_tags(text)
    draw_cloud(tags, 'wordcloud.png')

    text_file.close()


if __name__ == "__main__":
    main()