RDBMS 
# Model

객체관계매핑 : python과 sql을 연결

1. 모델 정의
# models.py
```python
    from django.db import models

    # DB내 컬럼명 저장
    class Post(models.Model):
        # 장고 라이브러리에 있는 models.Model을 상속받음.
        title = models.CharField(max_length=100)    # model안에 char 형이 들어갈 수 있는 변수 생성
        content = models.TextField(0)

        #ChrField : 상대적으로 짧은 글씨, TextField : 상대적으로
```

2. 번역본 생성
```bash
python manage.py makemigrations
```