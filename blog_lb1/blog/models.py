from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, 
        related_name='comment_author'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
