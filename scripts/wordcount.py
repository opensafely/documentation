from html.parser import HTMLParser
import sys


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.text = []

    def handle_starttag(self, tag, _):
        if tag == "article":
            self.in_article = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False

    def handle_data(self, data):
        if self.in_article:
            self.text.append(data)


if __name__ == "__main__":
    total = 0
    for filename in sys.argv[1:]:
        with open(filename, "r", encoding="utf-8") as f:
            parser = ArticleParser()
            parser.feed(f.read())
            text = " ".join(parser.text)
            total += len(text.split())
    print(total)
