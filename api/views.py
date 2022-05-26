from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view


from blog.models import Post
from .serializers import PostDetailSerializer, PostDeleteSerializer, PostCreateSerializer, PostListSerializer



class PostListOrCreateApiView(APIView):

    serializer_class = PostListSerializer

    def get_queryset(self):

        # post = self.get_object(request)
        # serializer = PostListSerializer(post)
        # return Response(serializer.data)

        # try:
            
            # ordering = request.GET.get('ordering' ,'newer')
            # sort = '-published_date' if ordering == 'newer' else 'published_date'
            # types = request.GET.get('types', 'published')
            # posts = Post.objects.all().annotate(comments_count=Count('comments'))
            # if type == 'published':
            #     posts.filter(published_date__isnull=False)
            # else:
            #     posts.filter(published_date__isnull=True)
        
    
        
        # return Response({"message": "OK"})

        # except Post.DoesNotExist:
        #     raise Http404


    

class PostDetailApiView(generics.RetrieveAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDetailSerializer
    



class PostDeleteApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDeleteSerializer
    







