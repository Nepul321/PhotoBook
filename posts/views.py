from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def PostListView(request, *args, **kwargs):
    context = {'request' : request}
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)