from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
        "likes_count",
    )

    list_filter = (
        "user",
    )

    def likes_count(self, tweet):
        return tweet.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
    )

    list_filter = (
        "user",
    )
