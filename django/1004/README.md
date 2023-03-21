# Django CRUD

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 '.gitignore'로 설정을 해둔다.

'''bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
'''

### 2. Django 설치 및 기록

'''
$ pip install django==3.2.13
$ pip freeze > requirements.txt
'''

### 3. Django 프로젝트 생성

'''bash
$ django-admin startproject pjt .
'''
'''bash
$ django-admin startproject pjt .
'''

## 2. articles app 생성

### 1. app 생성

### 2. app 등록

### 3. urls.py 설정

## 3. index

> url을 등록하고 view 함수 생성 , templates 만든다.

## 3. CRUD를 만들기 위해서 MODEL 정의하기 

## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

### 2. 마이그레이션 파일 생성 (python manage.py makemigrations)

### 3. DB 반영

## 4. CRUD 기능 구현

### 1. 게시판에 글 생성

> 사용자에게 HTML Form 제공, 입력한 데이터를 처리 (ModelForm 로직으로 변경해서 짤 수 있따)

#### 1. HTML Form 제공

http://127.0.0.1:8000/articles/new

#### 2. 입력 받은 데이터 처리

>http://127.0.0.1:8000/articles/create

#### 2-1. 요청과 관련된 수많은 데이터를 가지고 있는 객체 --> request를 이용

> 수많은 데이터를 객체에 담아서 보내주는 것이고 우리는 여기서 꺼내서 쓰는 것

> 게시글 DB에 저장하고 index 페이지로 redirect

### 2. 게시글 목록

> DB에서 게시글을 가져와서 template에 전달

### 3. 상세보기

> 특정한 글을 본다

>url 패턴이 id 값을 넣어줘야 한다.

예: http://127.0.0.1:8000/articles/<int:pk>/

즉, DB에 있는 특정한 값을 url에 넣어줘야 한다.

### 4. 삭제하기(직접해보기, 이전 수업 참고해서)

> 특정한 글을 삭제한다.

예: http://127.0.0.1:8000/articles/<int:pk>/delete/

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 있는 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> 예: http://127.0.0.1:8000/articles/<int:pk>/update/