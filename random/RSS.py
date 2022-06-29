import feedparser
NewsFeed = feedparser.parse("https://www.vesti.bg/rss")
entry = for news in NewsFeed
print(news)