import feedparser
import json
import re

# https://feedparser.readthedocs.io/en/latest/
# https://lincolnproject.libsyn.com/rss
rss_feed = input('Please enter the RSS link: ')

d = feedparser.parse(rss_feed)

for i in range(len(d.entries)):

    title=json.dumps(d.entries[i].title, indent=4)
    title=re.sub(r'(\\u2019)',"'", title).strip('"')
    print(f'TITLE: {title}')

    summary = json.dumps(d.entries[i].summary, indent=4)
    summary = re.sub(r'(<.*?>)','', summary)
    summary = re.sub(r'(\\u2019)',"'", summary).strip('"')
    print(f'SUMMARY: {summary}')

    link = json.dumps(d.entries[i]['links'][0].href, indent=4).strip('"')
    print(f'LINK: {link}')
    print('\n')


# print(d.feed.title)
# print(d.feed.link)
# print(d.feed.description)
# print(d.feed.published)
# print(d.feed.published_parsed)
# print(d.entries[0])
# print(json.dumps(d.entries[0], indent=4))