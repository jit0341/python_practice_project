#!/usr/bin/env python3
# 04_web_scraper.py
# Fetch a page and extract links using requests + BeautifulSoup

import argparse
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from pathlib import Path

USER_AGENT = "python-automation-example/1.0 (+https://example.com)"

def fetch(url, timeout=10):
    """Fetch URL and return response text (raises on HTTP errors)."""
    headers = {"User-Agent": USER_AGENT}
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text

def extract_links(html, base_url):
    """Return a list of absolute links found in the HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a['href'].strip()
        # build absolute URL
        abs_url = urljoin(base_url, href)
        links.append(abs_url)
    return links

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract links from a webpage")
    parser.add_argument("url", help="Page URL to scrape")
    parser.add_argument("--out", default="links.txt", help="Output file for links")
    parser.add_argument("--only-domain", action="store_true", help="Keep only links in the same domain")
    args = parser.parse_args()

    html = fetch(args.url)
    links = extract_links(html, args.url)

    if args.only_domain:
        domain = urlparse(args.url).netloc
        links = [l for l in links if urlparse(l).netloc == domain]

    # deduplicate while preserving order
    seen = set()
    uniq = []
    for l in links:
        if l not in seen:
            seen.add(l)
            uniq.append(l)

    Path(args.out).write_text("\n".join(uniq), encoding="utf-8")
    print(f"Wrote {len(uniq)} links to {args.out}")
