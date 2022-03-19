from rest_framework.response import Response
from rest_framework.decorators import (
    api_view, 
    permission_classes
)

from rest_framework.permissions import (
    IsAdminUser, 
    IsAuthenticated
)

from .serializers import (
    PostSerializer, 
    PostActionSerializer
)

from django.db.models import Q

from .models import Post


@api_view(['GET'])
def PostGlobalView(request, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.get_global_posts()
    serializer = PostSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
def PostSearchView(request, *args, **kwargs):
    context = {"request" : request}
    query = request.GET.get("q")
    if not query:
        return Response({"detail" : "Nothing searched"}, status=401)

    objects = Post.objects.filter(is_private=False)
    
    qs = objects.filter(
        Q(caption__contains=query) |
        Q(user__username__contains=query)

    )

    serializer = PostSerializer(qs, many=True, context=context)

    data = serializer.data

    return Response(data, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def PostListView(request, *args, **kwargs):
    context = {"request": request}
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)


@api_view(["GET"])
def UserPostsFeedView(request, *args, **kwargs):
    context = {"request": request}
    objects = []
    user = request.user
    qs = Post.objects.get_users_feed(user)
    for object in qs:
        if object.is_private == True:
            if object.user == user:
                objects.append(object)
        else:
            objects.append(object)

    serializer = PostSerializer(objects, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def PostCreateView(request, *args, **kwargs):
    context = {"request": request}
    post_data = request.data
    image = None
    try:
        image = post_data['image']
    except:
        pass
    if not image or image == "":
        return Response({"detail" : "No image"}, status=401)
    serializer = PostSerializer(data=post_data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        data = serializer.data
        return Response(data, status=201)

    return Response({}, status=401)


@api_view(["GET"])
def PostDetailView(request, id, *args, **kwargs):
    context = {"request": request}
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail": "Post not found"}, status=404)
    obj = qs.first()
    if obj.is_private == True:
        if obj.user == request.user:
            serializer = PostSerializer(obj, context=context)
            data = serializer.data
            return Response(data, status=200)
        return Response({"detail": "You don't have access to this post"}, status=403)
    serializer = PostSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def PostLikeUnlikeView(request, *args, **kwargs):
    context = {"request": request}
    serializer = PostActionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    id = data.get("id")
    action = data.get("action")
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail": "Post not found"}, status=404)
    obj = qs.first()
    if obj.is_private == True:
        if obj.user == request.user:
            if action == "like":
                obj.likes.add(request.user)
                serializer = PostSerializer(obj, context=context)
                return Response(serializer.data, status=200)
            elif action == "unlike":
                obj.likes.remove(request.user)
                serializer = PostSerializer(obj, context=context)
                return Response(serializer.data, status=200)
            else:
                return Response({"detail": "Action not valid"}, status=401)
    if action == "like":
        obj.likes.add(request.user)
        serializer = PostSerializer(obj, context=context)
        return Response(serializer.data, status=200)
    elif action == "unlike":
        obj.likes.remove(request.user)
        serializer = PostSerializer(obj, context=context)
        return Response(serializer.data, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def PostDeleteView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)

    obj = qs.first()
    if obj.user == request.user:
        obj.delete()
        return Response({"detail" : "Post deleted"}, status=200)

    return Response({"detail" : "You can't delete this post", "error" : 1}, status=403)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostUpdateView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)

    obj = qs.first()
    data = request.data
    image = data['image']
    if image == "":
        return Response({"detail" : "No image given"}, status=401)
    if obj.user == request.user:
        serializer = PostSerializer(instance=obj, data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    return Response({"detail" : "You can't update this post"}, status=403)
