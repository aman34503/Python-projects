import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()



#Now with this web scraper with Python, you can collect Google News headlines, the possibilities are endless. You can write a program to analyze the most used words in headlines. You can create a program to analyze stock sentiment and see if it correlates with the stock market.
# With this web scraper with Python, all the information in the world is yours, and I hope that turns you on as much as I do.