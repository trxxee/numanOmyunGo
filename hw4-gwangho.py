import requests
import re
import codecs

data = requests.get("http://rss.hankyung.com/new/news_main.xml")

title = re.compile("<title><!\[CDATA\[(.+)\]\]")
link = re.compile("<link><!\[CDATA\[(.+=r)")

news_title = title.findall(data.text)
news_link = link.findall(data.text)

# print(news_link)


f = codecs.open('hankyung_news.html','w','utf-8')
f.write(
    '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>GH_NEWS</title>
    <link href="hankyung_news.css"  rel="stylesheet" type="text/css" />
</head>
<body>
<h1> Team B <김민선, 이남진, 이광호> 한국경제 </h1>
'''
)

for num in range(14):
    f.write('<div id="title">'
    + news_title[num+1]
    + '</div>'
    + '<div id="link">'
    + '<a href="'+ news_link[num] + '">'
    + '링크바로가기'
    + '</a>'
    + '</div>'
    )

f.write("</body> </html>")

f.close()
