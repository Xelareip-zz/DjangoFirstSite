from django.db import models


class Tag(models.Model):
    name = models.CharField('Name', max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Title', max_length=150)
    post_date = models.DateField('Date')
    tags = models.ManyToManyField(Tag)
    content = models.TextField('Content', default='Empty post')

    def __str__(self):
        return self.title
