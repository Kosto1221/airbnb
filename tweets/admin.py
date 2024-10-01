from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    class MuskFilter(admin.SimpleListFilter):
        title = "Elon Musk included"

        parameter_name = "name"

        def lookups(self, request, model_admin):
            return [
                ("included", "Included"),
                ("excluded", "excluded"),
            ]

        def queryset(self, request, tweets):
            name=self.value()
            if name == "excluded":
                return Tweet.objects.exclude(payload__contains="Elon Musk")
            else:
                return tweets

    search_fields = (
        "payload",
        "user__username",
    )

    list_display = (
        "user",
        "payload",
        "likes_count",
    )

    list_filter = (
        MuskFilter,
        "user",
        "created_at",
    )

    def likes_count(self, tweet):
        return tweet.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    search_fields = (
        "user__username",
    )

    list_display = (
        "user",
        "tweet",
    )

    list_filter = (
        "user",
        "created_at",
    )
