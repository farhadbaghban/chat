from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import User, Message
from .serializers import MessageSerializer


class ChatView(APIView):
    def get(self, request, user_id):
        result = []
        user = User.objects.get(pk=user_id)
        senders = (
            user.received_messages.filter(is_read=False)
            .order_by("sender_id", "-timestamp")
            .distinct("sender_id")
        )
        for sender in senders:
            result.append(
                {
                    "username": sender.sender.username,
                    "id": sender.sender.id,
                    "first_name": sender.sender.first_name,
                    "last_name": sender.sender.last_name,
                    "unread_count": sender.sender.unread_count(),
                }
            )
        ser_data = MessageSerializer(instance=result, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    # def get_members(self, request, user_id):
    #     # TODO return all members associated with the user
