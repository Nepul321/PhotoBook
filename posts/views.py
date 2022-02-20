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

@api_view(['GET'])
def UserPostsFeedView(request, *args, **kwargs):
    context = {'request' : request}
    qs = Post.objects.get_users_feed()
    serializer = PostSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostCreateView(request, *args, **kwargs):
    context = {'request' : request}
    serializer = PostSerializer(data=request.data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        data = serializer.data
        return Response(data, status=201)

    return Response({}, status=401)

@api_view(['GET'])
def PostDetailView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Object not found"}, status=404)
    obj = qs.first()
    if obj.is_private == True:
        if obj.user == request.user:
            serializer = PostSerializer(obj, context=context)
            data = serializer.data
            return Response(data, status=200)
        return Response({"detail" : "You don't have access to this post"})
    serializer = PostSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)

    