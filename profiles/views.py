from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (
    Profile
)

from .serializers import (
    ProfileSerializer
)

@api_view(['GET'])
def ProfileListView(request, *args, **kwargs):
    context = {"request" : request}
    qs = Profile.objects.all()
    serializer = ProfileSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET', 'POST'])
def ProfileDetailView(request, username, *args, **kwargs):
    context = {"request" : request}
    qs = Profile.objects.filter(user__username=username)
    if not qs:
        return Response({"detail" : "Profile not found"}, status=404)
    obj = qs.first()
    serializer = ProfileSerializer(obj, context=context)
    data = request.data or {}
    if request.method == "POST":
        me = request.user
        action = data.get('action')
        if obj.user != me:
            if action == "follow":
                if me.is_authenticated == True:
                    obj.followers.add(me)
                    return Response(serializer.data, status=200)

                return Response({"detail" : "Login"}, status=403)
            elif action == "unfollow":
                if me.is_authenticated == True:
                    obj.followers.remove(me)
                    return Response(serializer.data, status=200)
                return Response({"detail" : "Login"}, status=403)

            else:
                pass        
    data = serializer.data
    return Response(data, status=200)