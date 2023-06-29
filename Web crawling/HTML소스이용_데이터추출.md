
```python
from bs4 import BeautifulSoup

html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
""" 

soup2 = BeautifulSoup(html2,"lxml")
```

```python
soup2.title

# 출력 : <title>작품과 작가 모음</title>
```


```python
soup2.body
# 출력 :
<body>
<h1>책 정보</h1>
<p id="book_title">토지</p>
<p id="author">박경리</p>
<p id="book_title">태백산맥</p>
<p id="author">조정래</p>
<p id="book_title">감옥으로부터의 사색</p>
<p id="author">신영복</p>
</body>
```

```python
soup2.body.h1
# 출력 : <h1>책 정보</h1>
```

```python
soup2.find_all('p')
# 출력 :

[<p id="book_title">토지</p>,
 <p id="author">박경리</p>,
 <p id="book_title">태백산맥</p>,
 <p id="author">조정래</p>,
 <p id="book_title">감옥으로부터의 사색</p>,
 <p id="author">신영복</p>]
```

```python
soup2.find('p',{"id":"book_title"})
# 출력 :
<p id="book_title">토지</p>
```

```python
soup2.find('p',{"id":"author"})
# 출력 :
[<p id="author">박경리</p>, <p id="author">조정래</p>, <p id="author">신영복</p>]
```

```python
soup2.find_all('p',{"id":"book_title"})
# 출력 :
 bs4.element.Tag
```

```python
book_titles=soup2.find_all('p',{"id":"book_title"})
authors=soup2.find_all('p',{"id":"author"})

for book_title,author in zip(book_titles,authors):
    print(book_title.get_text()+'/'+author.get_text())

    
#zip : 여러개를 가져오는 장치

print(book_titles) # 리스트로 출력


# 출력 :
토지/박경리
태백산맥/조정래
감옥으로부터의 사색/신영복
[<p id="book_title">토지</p>, <p id="book_title">태백산맥</p>, <p id="book_title">감옥으로부터의 사색</p>]
```



