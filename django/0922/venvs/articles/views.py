from django.shortcuts import render
import random
# Create your views here.
def index(request):

    names =['엄태동','누구누구','환영환영']
    name = random.choice(names)
    context={
        'name' : '엄태동',
        # 'name':name, 랜덤함수로 리스트에 있는 string 중 하나 넣기
        'img' : 'https://www.google.ca/url?sa=i&url=https%3A%2F%2Fwww.crowdpic.net%2Fphoto%2F%25ED%2599%2598%25EC%2598%2581%25ED%2595%25A9%25EB%258B%2588%25EB%258B%25A4-%25EC%25BA%2598%25EB%25A6%25AC%25EA%25B7%25B8%25EB%259D%25BC%25ED%2594%25BC-%25EC%259E%2585%25ED%2595%2599%25EC%258B%259D-%25EB%2582%2598%25EB%25AD%2587%25EC%259E%258E-%25EC%258B%259C%25EC%259E%2591-884507&psig=AOvVaw1u_QgXciRUxOgbv7_xEN8O&ust=1669688166431000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCJjfv6Lnz_sCFQAAAAAdAAAAABAD'
    }
    return render(request, 'index.html', context)

def welcom(request, name):  # urls.py에서 정의한 <name>에서 name이라는 값을 쓰겠다는 의미
    # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    context ={
        'name':name,
        'greetings':['안녕하세요','bonjour','니하오'], # 홈페이지에 한줄한줄 저 인삿말을 보여주고 싶다
    }
    return(request, 'welcome.html', context)