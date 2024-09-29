from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
    )

    list_filter = (
        "user",
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
    )

    list_filter = (
        "user",
    )
