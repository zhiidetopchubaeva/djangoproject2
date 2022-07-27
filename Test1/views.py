from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post1

@api_view(['GET'])
def posts_list1(request):
    queryset = Post1.objects.all()
    serializer = PostSerializer(instance=queryset, many=True)
    return Response(serializer.data)
