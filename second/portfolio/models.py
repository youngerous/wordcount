from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    # 이미지를 데이터베이스에 넣고 싶을 때
    # pip install pillow

    def __str__(self):
        return self.title