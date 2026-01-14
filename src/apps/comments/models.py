from django.db import models
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(
        'posts.Post',   # چون Post در اپ دیگر است
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def clean(self):
        existing_comments = Comment.objects.filter(post=self.post, author=self.author).count()
        if self.pk is None and existing_comments >= 10:
            raise ValidationError("You cannot add more than 10 comments to this post.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
