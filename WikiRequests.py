from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def getWikiPageWords(input):
    url_prefix = 'https://en.wikipedia.org/wiki/'
    html = urlopen(url_prefix + input)
    soup = BeautifulSoup(html, 'html.parser')
    all_ps = soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs, limit=5)
    all_ps = [s.get_text() for s in all_ps]
    all_ps = ' '.join(all_ps)
    # gets rid of all [1], [23], etc type strings.
    after_sub = re.sub("(\\[\\d+])|(\\n)", "", all_ps)
    return after_sub