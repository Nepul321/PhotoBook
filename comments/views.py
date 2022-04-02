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


@api_view(["GET", "DELETE", "POST"])
def CommentDetailView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Comment not found"}, status=404)
    obj = qs.first()
    user = request.user
    if request.method == "DELETE":
        if user.is_authenticated:
            if user == obj.user:
                obj.delete()
                return Response({"detail" : "Comment deleted"}, status=200)
            return Response({"detail" : "You can't delete this comment"}, status=403)
        return Response({"detail" : "You can't delete this comment"}, status=403)
    if request.method == "POST":
        if user.is_authenticated:
            if user == obj.user:
                data = request.data
                serializer = CommentSerializer(instance=obj, data=data, context=context)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=200)
            return Response({"detail" : "You can't update this comment"}, status=403)
        return Response({"detail" : "You can't update this comment"}, status=403)
            
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