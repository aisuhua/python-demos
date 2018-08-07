from django.db import models

# Create your models here.


class Topic(models.Model):
    """日志主题分类"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """日志条目"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """重写复数的表示形式"""
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
