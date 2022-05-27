from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from django.http import Http404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist



from blog.models import Post
from .serializers import PostDeleteSerializer, PostCreateSerializer, PostListSerializer


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
class PostListApiView(APIView):

    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):

        try:
            ordering = request.GET.get('ordering' ,'newer')
            sort = '-published_date' if ordering == 'newer' else 'published_date'
            types = request.GET.get('types', 'published')
            posts = Post.objects.all().annotate(comments_count=Count('comments'))
            if types == 'published':
                posts.filter(published_date__isnull=False)
            else:
                posts.filter(published_date__isnull=True)
        
            data = Serializer(sort, many=True).data
            return Response(
                data
                # posts,
                # sort,
                # status=status.HTTP_404_NOT_FOUND,
            )
        except ObjectDoesNotExist:
            raise Http404


    

class PostCreateApiView(APIView):

    serializer_class = PostCreateSerializer
    
    def post(self, request, *args, **kwargs):
        pass






class PostDeleteApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDeleteSerializer
    







