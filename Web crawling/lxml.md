```python
!pip install cssselect
!pip install lxml

import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)

for a in root.cssselect('.view_box a'):
    url=a.get('href')
    print(url)
```
-----------------------------------------------------------------

```python
!pip install lxml
!pip install requests
!pip install cssselect


from typing import get_args
import requests
from lxml.html import fromstring, tostring

def main():
    
    session = requests.Session()
    response = session.get("https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
    urls = scrape_news_list_page(response)
    
    for name, url in urls.items():
        print(name, url)

        
def scrape_news_list_page(response):
    urls={}
    roots = fromstring(response.content)
    
    for a in root.xpath('//ul[@class="basic1"]/li/dl/dt/a[@class="_nclicks:kin.txt _searchListTitleAnchor"]')
        name, url = extract_conents(a)
        urls[name]=url
    
    return urls
                        
def extract_conents(doc):
    link=doc.get("herf")
    name=doc.text_content()
return name, link
                        
if __name__ == '__main__':
    main()
```
