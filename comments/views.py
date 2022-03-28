from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Comment
from .serializers import CommentListSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def CommentListView(request, *args, **kwargs):
    context = {"request" :  request}
    qs = Comment.objects.all()
    serializer = CommentListSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)