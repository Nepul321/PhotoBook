from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from django.db.models import Q

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

@api_view(["GET"])
def PostCommentsView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.filter(
        Q(id=id),
        Q(is_private=False)
    )
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)
    obj = qs.first()
    commentsFinal = []
    commentQs = Comment.objects.filter(post=obj)
    for comment in commentQs:
        if comment.is_child == False:
            commentsFinal.append(comment)

        
    serializer = CommentSerializer(commentsFinal, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CommentCreateView(request, post_id, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.filter(id=post_id)
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)
    obj = qs.first()
    data = request.data
    parent = data['parent'] or None
    if parent:
        commentQs = Comment.objects.filter(id=parent)
        if not qs:
            return Response({"detail" : "Comment not found"}, status=404)
        commentObj = commentQs.first()
    else:
        commentObj = None
    serializer = CommentSerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            post=obj,
            user=request.user,
            parent=commentObj
        )

        return Response(serializer.data, status=201)
    
    return Response({}, status=401)