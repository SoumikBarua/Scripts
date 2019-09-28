# Standard library import
import urllib.request

# 3rd-party import
from bs4 import BeautifulSoup

def top_10_news_articles():
    """Scrapes/crawls the Google finance news section and writes to a
    file the title, source and dates of the top ten articles.
    NOTE: the URL and the HTML content may have changed since the
    writing of this."""

    request = urllib.request.urlopen("https://finance.google.com/finance/market_news")
    soup = BeautifulSoup(request, "html.parser")
    print(soup.prettify())

    file = open("file_ops_6_output.txt", "w")

    news_container = soup.find.all(class_="g-section news sfe-break-bottom-16")
    for each in news_container:
        title.append(each.find(class_="name").get_text().strip("\n").replace(u'\xa0', u' '))
    for each in soup.find_all('div', class_="byline"):
        for src in each.find_all("span", class_="src"):
           source.append(src.text)
    for each in soup.find_all("span", class_="date"):
        date.append(each.text)

    print(date)
    
    for x in range(0, len(title)):
        file.write(title[x])
        file.write(', ')
        file.write(source[x])
        file.write(', ')
        file.write(date[x])
        file.write("\n")

    file.close()

top_10_news_articles()
