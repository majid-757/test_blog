from django.shortcuts import render
from rest_framework import generics



from blog.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostDeleteSerializer


class PostListApiView(generics.ListAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostListSerializer

    

class PostDetailApiView(generics.RetrieveAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDetailSerializer
    # lookup_field = 'id'



class PostDeleteApiView(generics.DestroyAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDeleteSerializer
    lookup_field = 'id'







