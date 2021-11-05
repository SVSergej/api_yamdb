from django.contrib import admin

from models import Review, Comments


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'title_id', 'text')
    # search_fields = ('text',)
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'review_id', 'text', 'author', 'pub_date')
    # search_fields = ('text',)
    pass
