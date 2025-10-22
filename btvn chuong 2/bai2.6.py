import requests

rss_url="http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
respone= requests.get(rss_url)
if respone.status_code==200:
    with open("tep_xml.xml","wb") as file:
        file.write(respone.content)
    print("đã lưu thành công")
else:
    print("có lỗi khi lưu", respone.status_code)

import xml.dom.minidom

def main():
    doc=xml.dom.minidom.parse("tep_xml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

if __name__=="__main__":
    main()

import csv
with open("tep_tin.csv", mode="w", newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(file, filenames=["title","link","description","pubDate"])
    writer.writeheader()

    writer.writerow("tep_tin")

print("đã lưu danh sách")