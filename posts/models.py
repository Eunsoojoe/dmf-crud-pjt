from django.db import models

# DB내 컬럼명 저장
class Post(models.Model):
    # 장고 라이브러리에 있는 models.Model을 상속받음.
    title = models.CharField(max_length=100)    # model안에 char 형이 들어갈 수 있는 변수 생성
    content = models.TextField(0)

    #ChrField : 상대적으로 짧은 글씨, TextField : 상대적으로