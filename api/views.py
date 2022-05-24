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
    



class PostDeleteApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()    
    serializer_class = PostDeleteSerializer
    







