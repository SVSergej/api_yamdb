from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

Titles = None
Users = None


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='title_review',
    )
    text = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='author_review',
    )
    score = models.SmallIntegerField()  # if 1 <= score <= 10
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='review_comment',
    )
    text = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='author_comment'
    )
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text
