from django.db import models
from common.models import CommonModel

# Create your models here.
class Tweet(CommonModel):
    """Tweet Model Definition"""

    payload = models.CharField(
        max_length=180,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(tweet):
        return str(tweet.user)

class Like(CommonModel):
    """Like Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(like):
        return str(like.user)


