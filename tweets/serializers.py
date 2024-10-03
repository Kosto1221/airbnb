from rest_framework import serializers
# from .models import Tweet

class AllTweetsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user = serializers.CharField(
        required=True
    )
    payload = serializers.CharField(
        max_length=180,
    )
    created_at = serializers.DateTimeField(read_only=True)

class UsersTweetsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
    payload = serializers.CharField(
        max_length=180,
        read_only=True
    )
    created_at = serializers.DateTimeField(read_only=True)
