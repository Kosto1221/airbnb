from django.urls import path
from . import views

urlpatterns = [
    path("tweets", views.see_all_tweets),
    path("users/<str:user>/tweets", views.see_user_tweets),
]