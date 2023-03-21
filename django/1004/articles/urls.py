# urls 설정을 app 단위로!
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns =[
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>',views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'), # detail 페이지에서 수정하도록 설계해보자
]