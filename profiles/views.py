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

@api_view(['GET'])
def ProfileDetailView(request, username, *args, **kwargs):
    context = {"request" : request}
    qs = Profile.objects.filter(user__username=username)
    if not qs:
        return Response({"detail" : "Profile not found"}, status=404)
    obj = qs.first()
    serializer = ProfileSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)