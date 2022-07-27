from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post2

@api_view(['GET'])
def posts_list2(request):
    queryset = Post2.objects.all()
    serializer = PostSerializer(instance=queryset, many=True)
    return Response(serializer.data)