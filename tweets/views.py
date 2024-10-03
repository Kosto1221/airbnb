# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Tweet
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AllTweetsSerializer, UsersTweetsSerializer
from rest_framework.exceptions import NotFound

# Create your views here.
@api_view()
def see_all_tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = AllTweetsSerializer(all_tweets, many=True)
    return Response(serializer.data)

@api_view()
def see_user_tweets(request, user):
    try:
        validate_user = User.objects.get(username=user)
        tweets = Tweet.objects.filter(user__username=validate_user)
    except User.DoesNotExist:
        raise NotFound
    serializer = UsersTweetsSerializer(tweets, many=True)
    return Response(serializer.data)
    