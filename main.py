import feedparser

# https://feedparser.readthedocs.io/en/latest/

rss_feed = r'https://lincolnproject.libsyn.com/rss'

d = feedparser.parse(rss_feed)

print(d.feed.title)

print(d.feed.link)

print(d.feed.description)

print(d.feed.published)

print(d.feed.published_parsed)