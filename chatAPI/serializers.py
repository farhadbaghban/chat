from rest_framework import serializers
from .models import Message


# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = "__all__"


class MessageSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    unread_count = serializers.IntegerField()
