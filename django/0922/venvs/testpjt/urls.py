"""testpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views      # articles 폴더의 views 파일을 불러오겠다
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),     # views 파일 내의 index 함수로 index 페이지를 핸들링 하겠다 """
    path('welcome/<name>',views.welcome), # welcom이라는 함수로 <>안의 name을 활용하겠다.
]
