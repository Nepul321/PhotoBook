from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Comment
from .serializers import CommentSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def CommentListView(request, *args, **kwargs):
    context = {"request" :  request}
    qs = Comment.objects.all()
    serializer = CommentSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)


@api_view(["GET"])
def CommentDetailView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Comment not found"}, status=404)
    obj = qs.first()
    serializer = CommentSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)
