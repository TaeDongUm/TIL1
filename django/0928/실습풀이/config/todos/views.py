from django.shortcuts import render, redirect
from .models import Todo


def index(request):
  todos = Todo.objects.all()

  context = {
    'todos' : todos,
  }
  return render(request, 'todos/index.html', context)

def create(request):
  # form 태그를 사용해서 데이터 송수신
  content = request.GET.get('content')  # index.html에서 content 이름으로 입력한 값을 받겠다
  priority = request.GET.get('priority')
  deadline = request.GET.get('deadline')
  
  # Todo.objects.create() 를 사용해서 데이터를 추가
  Todo.objects.create(
    content = content,
    priority = priority,
    deadline = deadline,
  )

  return redirect('todos:index')
   
def delete(request, todo_pk):
  todo = Todo.objects.get(pk = todo_pk) # 삭제할 값을 불러오기
  todo.delete()
  """
  리다이렉트
  1. 사용자가 create 요청
  2. 서버에서 index 요청
  3. 사용자에게는 index 응답
  """
  return redirect('todos:index')


def update(request, pk):
  todo = Todo.objects.get(pk = pk)

  # True -> False
  # False -> True
  todo.completed = not todo.completed
  
  todo.save()
  return redirect('todos:index')
