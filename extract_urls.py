import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='URL extraction tool')
parser.add_argument('url', type=str, help='URL to extract')
parser.add_argument('--depth', type=int, default=1, help='Recursion depth')
args = parser.parse_args()


def extract_urls(url, depth):
    if depth == 0:
        return []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = [link.get('href') for link in soup.find_all('a')]
        urls = [u for u in urls if u is not None]
        urls = [u for u in urls if u.startswith(
            'http') or u.startswith('https')]
        sub_urls = []
        for u in urls:
            sub_urls += extract_urls(u, depth - 1)
        return urls + sub_urls
    except:
        return []


urls = extract_urls(args.url, args.depth)

with open("urls.txt", "a") as f:
    for url in urls:
        print(url, file=f)
        print(url)
