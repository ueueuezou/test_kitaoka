from django.db import models

from datetime import datetime


CATEGORY = (('everyday', '日常'), ('question', '質問'), ('other', 'その他'))
class Com(models.Model):
    created = models.DateTimeField(default=datetime.now())
    category = models.CharField(
               max_length=100,
               choices = CATEGORY
               )
    image = models.ImageField(null=True, blank=True, upload_to='upload/', default='upload/1896615.jpg')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Comment(models.Model):
    com = models.ForeignKey(Com, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now())
    text = models.TextField(max_length=500)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class News(models.Model):
    created = models.DateTimeField(default=datetime.now())
    text = models.TextField(max_length=100)

class Link(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')
    text = models.TextField(max_length=300)