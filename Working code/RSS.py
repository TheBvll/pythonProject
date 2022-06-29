import feedparser
Newsfeed = feedparser.parse("https://www.vesti.bg/rss")
Newsfeed2 = feedparser.parse("https://www.budilnik.com/feed/")
Newsfeed3 = feedparser.parse("https://www.struma.com/rss/")


entry = Newsfeed.entries[1]
entry1 = Newsfeed.entries[2]
entry2 = Newsfeed.entries[3]
entry3 = Newsfeed.entries[4]
entry4 = Newsfeed.entries[5]
entry5 = Newsfeed.entries[6]
entry6 = Newsfeed.entries[7]
entry7 = Newsfeed.entries[8]
entry8 = Newsfeed.entries[9]
entry9 = Newsfeed.entries[10]

entry10 = Newsfeed2.entries[1]
entry11 = Newsfeed2.entries[2]
entry12 = Newsfeed2.entries[3]
entry13 = Newsfeed2.entries[4]
entry14 = Newsfeed2.entries[5]
entry15 = Newsfeed2.entries[6]
entry16 = Newsfeed2.entries[7]
entry17 = Newsfeed2.entries[8]
entry18 = Newsfeed2.entries[9]
entry19 = Newsfeed2.entries[10]

entry20 = Newsfeed3.entries[1]
entry21 = Newsfeed3.entries[2]
entry22 = Newsfeed3.entries[3]
entry23 = Newsfeed3.entries[4]
entry24 = Newsfeed3.entries[5]
entry25 = Newsfeed3.entries[6]
entry26 = Newsfeed3.entries[7]
entry27 = Newsfeed3.entries[8]
entry28 = Newsfeed3.entries[9]
entry29 = Newsfeed3.entries[10]


print("================VESTI================")
print(entry.published)
print(entry.summary)
print(entry.link)

print(entry1.published)
print(entry1.summary)
print(entry1.link)

print(entry2.published)
print(entry2.summary)
print(entry2.link)

print(entry3.published)
print(entry3.summary)
print(entry3.link)

print(entry4.published)
print(entry4.summary)
print(entry4.link)

print(entry5.published)
print(entry5.summary)
print(entry5.link)

print(entry6.published)
print(entry6.summary)
print(entry6.link)

print(entry7.published)
print(entry7.summary)
print(entry7.link)

print(entry8.published)
print(entry8.summary)
print(entry8.link)

print(entry9.published)
print(entry9.summary)
print(entry9.link)
print("================VESTI================")

print("================BUDILNIK================")
print(entry10.published)
print(entry10.summary)
print(entry10.link)

print(entry11.published)
print(entry11.summary)
print(entry11.link)

print(entry12.published)
print(entry12.summary)
print(entry12.link)

print(entry13.published)
print(entry13.summary)
print(entry13.link)

print(entry14.published)
print(entry14.summary)
print(entry14.link)

print(entry15.published)
print(entry15.summary)
print(entry15.link)

print(entry16.published)
print(entry16.summary)
print(entry16.link)

print(entry17.published)
print(entry17.summary)
print(entry17.link)

print(entry18.published)
print(entry18.summary)
print(entry18.link)

print(entry19.published)
print(entry19.summary)
print(entry19.link)
print("================BUDILNIK================")

print("================STRUMA================")
print(entry20.published)
print(entry20.summary)
print(entry20.link)

print(entry21.published)
print(entry21.summary)
print(entry21.link)

print(entry22.published)
print(entry22.summary)
print(entry22.link)

print(entry23.published)
print(entry23.summary)
print(entry23.link)

print(entry24.published)
print(entry24.summary)
print(entry24.link)

print(entry25.published)
print(entry25.summary)
print(entry25.link)

print(entry26.published)
print(entry26.summary)
print(entry26.link)

print(entry27.published)
print(entry27.summary)
print(entry27.link)

print(entry28.published)
print(entry28.summary)
print(entry28.link)

print(entry29.published)
print(entry29.summary)
print(entry29.link)
print("================STRUMA================")
