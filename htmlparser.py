from html.parser import HTMLParser

class MyHtmlParser(HTMLParser) :
    def handle_starttag(self, tag, attrs) :
        print(tag)
        [print('-> '+ attr[0]+ ' > '+ attr[1] ) for attr in attrs]

parser = MyHtmlParser()
html = '\n'.join( [input() for _ in range(int(input()))])
print(html)
parser.feed(html);