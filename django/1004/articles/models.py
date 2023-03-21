from django.db import models

# Create your models here.
'''
게시판 기능
- 제목(20글자 이내)
- 내용
- 글 작성시간/수정시간
'''
# 1. 모델 설계 ( DB 스키마 설계 )
# 클래스 정의
# 모델 상속받기, 모델 설계는 하되 장고에서 주어지는 기능들은 쓰고 싶어서
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    # 생성 시간
    # 생성될 떄 수정될 떄 자동으로 기록
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

