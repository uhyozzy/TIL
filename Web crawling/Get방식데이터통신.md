## 1)
```python
import urllib.request
import urllib.parse

url = "http://www.encar.com/"
mem = urllib.request.urlopen(url)

API = "https://api.ipify.org"

values = {
    'format':'json'
}

print('before param: {}'.format(values))
params=urllib.parse.urlencode(values)
print('after param: {}'.format(params))

url = API + "?" + params

data = urllib.request.urlopen(url).read()


text = data.decode("utf-8")
print('response : {}'.format(text))
```

## 2) RSS
```python
import urllib.request
import urllib.parse

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))
    
    
for c in params:
    param = urllib.parse.urlencode(c)
    url = API + "?" + param
    print("url=", url)
    res_data = urllib.request.urlopen(url).read()
    contents = res_data.decode("utf-8")
    print(contents)
```
