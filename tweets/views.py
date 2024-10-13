# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Tweet
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from . import serializers

class Tweets(APIView):
    
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            new_tweet = serializer.save()
            return Response(TweetSerializer(new_tweet).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

class TweetDetail(APIView):

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = serializers.TweetSerializer(tweet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tweet = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if tweet.user != request.user:
            raise PermissionDenied
        serializer = TweetSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
    
    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if tweet.user != request.user:
            raise PermissionDenied
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
