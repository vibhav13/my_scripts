import requests
import re
from urllib.parse import urljoin


# regular expression for link
link_re = re.compile(r'href="(.*?)"')


def crawl(url):

    req = requests.get(url)

    # check for status 200
    if(req.status_code != 200):
        return []

    # collect links
    links = link_re.findall(req.text)

    print("Links are {} ".format(len(links)))

    for link in links:

        # Get absolute URL
        link = urljoin(url, link)

        print(link)

if __name__ == '__main__':
    crawl('http://www.srivastavavibhav.com')
