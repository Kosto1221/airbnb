# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Tweet
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT

class Tweets(APIView):
    
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save()
            return Response(TweetSerializer(new_tweet).data)
        else:
            return Response(serializer.errors)
        
class UserTweets(APIView):

    def get_object(self, username):
        try:
            validate_user = User.objects.get(username=username)
            tweets = Tweet.objects.filter(user__username=validate_user)
        except User.DoesNotExist:
            raise NotFound
        return tweets
        
    def get(self, request, username):
        serializer = TweetSerializer(self.get_object(username), many=True)
        return Response(serializer.data)
    
    def post(self, request, username):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save()
            return Response(TweetSerializer(new_tweet).data)
        else:
            return Response(serializer.errors)

class TweetDetail(APIView):

    def get_object(self, tweet_id, username):
        try:
            validate_user = User.objects.get(username=username)
            tweet = Tweet.objects.get(user=validate_user, id=tweet_id)
        except User.DoesNotExist:
            raise NotFound
        except Tweet.DoesNotExist:
            raise NotFound
        return tweet
        
    def get(self, request, tweet_id, username):
        serializer = TweetSerializer(self.get_object(tweet_id, username))
        return Response(serializer.data)
    
    def put(self, request, tweet_id, username):
        serializer = TweetSerializer(self.get_object(tweet_id, username), data=request.data, partial=True)
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, tweet_id, username):
        self.get_object(tweet_id, username).delete()
        return Response(status=HTTP_204_NO_CONTENT)
