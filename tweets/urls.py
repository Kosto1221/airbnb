from django.urls import path
from . import views

urlpatterns = [
    path("tweets", views.Tweets.as_view()),
    path("users/<str:username>/tweets", views.UserTweets.as_view()),
    path('users/<str:username>/tweets/<int:tweet_id>/', views.TweetDetail.as_view()),
]