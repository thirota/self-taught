
import ssl
import certifi
import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # fix: unable to get local issuer certificate
        #r = urllib.request.urlopen(self.site)
        r = urllib.request.urlopen(self.site, context=ssl.create_default_context(cafile=certifi.where()))
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)



news = "https://news.google.com/"
Scraper(news).scrape()
 

