from django.shortcuts import render, redirect
from .models import Article # models.py에 있는 클래스 Article을 불러오겠습니다
from django.forms import ModelForm
from .forms import ArticleForm
# Create your views here.

# 요청 정보를 받아서 페이지를 render
def index(request):
    # 게시글을 가져와서
    articles=Article.objects.all()

    # # 게시글을 가져와서 역순으로 넘겨주기
    # articles=Article.objects.order_by('-pk')

    # template에 전달한다. 
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     # forms.py에서 작성했던 클래스를 이용해서 값을 넘겨받고 싶다
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)

# def create(request):
#     # DB에 저장하기
#     # GET은 정보 조회할 때 쓰이고
#     # DB에 저장하기 위해서 POST 씀
#     # 로그인 정보가 url 상에 나타나면 안되기 때문에
#     title=request.POST.get('title')
#     content = request.POST.get('content')

    #& 많은 정보가 입력되면 그만큼 fields를 request.POST 일일이 다 해야 함, render를 통해서도 많은 값을 넘겨줘야 함


#     Article.objects.create(title=title, content=content) # Article 클래스 정의하면서 title, content로 정의했으니 여기로 받기
#     return redirect('articles:index')

# def create(request):
#      #& 단순히 request.POST값을 article_form에 넘겨줘버린다
#     article_form = ArticleForm(request.POST)
#     if article_form.is_valid():  # article_form의 유효성 검사
#         article_form.save()         # 유효하면 저장하기
#         return redirect('articles:index')
#     else:
#         print('유효하지 않습니다.')
#         context = {
#         'article_form': article_form
#         }
#         # 유효하지 않을 떄 그 페이지 그대로 보여주고 동시에 쓰던 데이터 또한 그대로
#         return render(request, 'articles/new.html', context=context)

#! 기존의 Create와 New를 합친 것
def create(request):
    print(request.method)
    if request.method == "POST":
        print("request.method")
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid() :  # article_form의 유효성 검사
            article_form.save()         # 유효하면 저장하기
            return redirect('articles:index')
    else:
        # 기존의 new와 같다
        article_form = ArticleForm()
    # 유효성 검사 후 유효하지 않으면 다시 작성하게끔
    context = {
    'article_form': article_form
    }
    # 유효하지 않을 떄 그 페이지 그대로 보여주고 동시에 쓰던 데이터 또한 그대로
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    # 특정 글을 가져온다
    article = Article.objects.get(pk=pk)

    #  template에 객체 전달
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk) # 수정하기 위해서 이전 글을 불러와야 하므로
    if request.method == "POST":
        # POST : input 값 가져와서 검증하고 DB에 저장
        # 기존에 있는 값을 수정하므로 그 기존값을 받아와야 한다. 없으면 수정이 아니라 글을 생성함
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 상세보기 페이지로
            return redirect('articles:detail', article.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:        
        # GET : forms을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/update.html', context)