요약내용 출처
[깃허브](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# 1. 제목 설정하기 
'# 제목1 - 대주제

'## 제목2 - 중간주제

'### 제목3 - 소주제


# 2. 글자 형식 지정하기 

#굵게 : ** **
ex. **Bold**

# 3. 인용구 작성하기
## 꺽세 인용하기 
>이것이 인용이다


## 홑따옴표 이용하기
```
인용코드
홑따옴표가 아니라 백틱임(물결표시 자리에 있음)
```
# 4. 파일 첨부하기
## 링크 첨부하기 
#문법 : [링크제목](url)

[GitHub Pages](https://pages.github.com/).


## 사진 첨부하기
#사진 첨부
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

>!를 추가하고 []안에 텍스트를 넣어 이미지를 표시할 수 있음. 이미지에 대한 링크를 ()로 래핑하기

# 4. 목록 지정하기 
#"*", "+", 곱하기나 플러스 표시를 사용하여 하나 이상의 텍스트 줄앞에 정렬되지 않은 목록을 만들 수 있음
```
- George Washington
* John Adams
+ Thomas Jefferson
```

#목록의 순서를 지정하려면 각 줄 앞에 숫자 입력 
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```

#중첩된 목록도 사용 가능
> 목록 표식 문자(- 또는 *)가 해당 항목의 첫 번째 문자 바로 아래에 놓일 때까지 중첩된 목록 항목 앞에 공백 문자를 입력
```
1. First list item
   - First nested list item
     - Second nested list item

```

#5. 작업목록 작성하기
>작업 목록을 만들려면 하이픈과 공백 뒤에 [ ]이 오는 목록 항목의 접두사를 설정합니다. 작업을 완료로 표시하려면 [x]를 사용합니다.
```
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```
