from django.db import models

# Create your models here.
class Question(models.Model):
    #질문은 제목과 두 가지 선택지가 필요하므로 3개의 필드로 구성
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)


class Comment(models.Model):
    #comment는 question과 1:N 관계
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    # pick = models.IntegerField()
    content = models.CharField(max_length=100)