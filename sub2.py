import codecs
import requests
import re

res = requests.get("https://search.naver.com/search.naver?where=nexearch&query=%ED%99%98%EC%9C%A8&sm=top_hty&fbm=1&ie=utf8")
country = '''<span>([가-힣]+) <em>'''
cou = re.compile(country)
cou_list = cou.findall(res.text)


rate = '''<strong>([\d\,\.]+)<\/strong> <span>'''
r = re.compile(rate)
rate_list = r.findall(res.text)

yesterday = '''(.)[<\/span>]* [<span>]*([\d\.]+)<\/span><\/span><\/h3>'''
yes = re.compile(yesterday)
yes_list = yes.findall(res.text)
for arrow in yes_list[0]:
    if arrow == '"':
        arrow = '-'

remain = '''<span class="percent \w+">(.?\d.\d+%)<\/span><\/td> <td>((\d,)?\d+.\d+)<\/td> <td>((\d,)?\d+.\d+)<\/td> <td>((\d,)?\d+.\d+)<\/td> <td>((\d,)?\d+.\d+)<\/td> <td class="last"><a nocr'''
rem = re.compile(remain)
rem_list = rem.findall(res.text)


f=codecs.open("index.html", 'w', 'utf-8')

f.write("""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table border="1">
    <tr>
        <th>국가</th>
        <th>환율</th>
        <th>전일대비</th>
        <th>등락율</th>
        <th>현찰(살때)</th>
        <th>현찰(팔때)</th>
        <th>송금(보낼때)</th>
        <th>송금(받을때)</th>
        """)
for i in range(7):
    f.write('<tr align = "right"> <td>'
            + '<a href="http://info.finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW">' + cou_list[i] + "</a> </td> <td>"
            + rate_list[i] + "</td> <td>"
            + (yes_list[i])[0]+(yes_list[i])[1] + "</td> <td>"
            + (rem_list[i])[0] + "</td> <td>"
            + (rem_list[i])[1] + "</td> <td>"
            + (rem_list[i])[3] + "</td> <td>"
            + (rem_list[i])[5] + "</td> <td>"
            + (rem_list[i])[7] + "</td> </tr>")

f.write("""</table> </body> </html>""")

f.close()