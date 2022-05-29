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
from django.shortcuts import render


from blog.models import Post, Comment, AboutUs
from .serializers import (
    PostDeleteSerializer, 
    PostCreateSerializer, 
    PostListSerializer, 
    PostDetailSerializer,
    PostEditSerializer,
    PostDraftListSerializer,
    AddCommentToPostSerializer,
    CommentRemoveSerializer,
    CommentApproveSerializer,
    AboutUsSerializer,
)


# try:
#     post = Post.objects.get(id=1)
# except Post.DoesNotExist:
#     return Response(status=404)



class PostListApiView(APIView):

    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):

        try:
            ordering = request.GET.get('ordering' ,'newer')

            if ordering == 'newer':
        
        # posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
                sort = '-published_date'
        

    # posts = Post.objects.filter(name__contains=ordering)
            elif ordering == 'older':

        # posts = Post.objects.filter(published_date__isnull=False).order_by('created_date')
                sort = 'published_date'

            posts = Post.objects.filter(published_date__isnull=False).order_by(sort)

            # else:

            #     posts = Post.objects.all()

    

            types = request.GET.get('types', 'published')

            if types == 'published':

        # posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
        
                posts = Post.objects.filter(published_date__isnull=False).order_by(sort)

            elif types == 'draft':

        # posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        
                posts = Post.objects.filter(published_date__isnull=True).order_by(sort)

            else:

                posts = Post.objects.all()
        
            data = self.serializer_class(posts, many=True).data
            return Response(
                data,
                # posts,
                # sort,
                # status=status.HTTP_404_NOT_FOUND,
            )
        except ObjectDoesNotExist:
            raise Http404


    

class PostCreateApiView(APIView):

    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            post = serializer.save(author=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class PostDetailApiView(APIView):

    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk, author_id=request.user.id)
            serializer = self.serializer_class(post)

        except Post.DoesNotExist:

            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDeleteApiView(APIView):

    serializer_class = PostDeleteSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        try:
            post = Post.objects.get(pk=pk, author_id=request.user.id)
            serializer = self.serializer_class(post)
            post.delete()

        except Post.DoesNotExist:

            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)





class PostEditApiView(APIView):

    serializer_class = PostEditSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk,*args, **kwargs):

        try:
            post = Post.objects.get(pk=pk, author_id=request.user.id)
            serializer = self.serializer_class(post, data=request.data)
            
            if serializer.is_valid():
                # serializer.data
                # serializer.validated_data
                serializer.save()
            else:
                return Response({'message': 'invalid'})

        except Post.DoesNotExist:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)




class PostDraftListApiView(APIView):

    serializer_class = PostDraftListSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):

        post = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        serializer = self.serializer_class(post, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
        


class AddCommentToPostApiView(APIView):

    serializer_class = AddCommentToPostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:
            # comment = Comment.objects.get(pk=pk, author=request.user.id)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                return Response({'message': 'invalid'})
            
        except Comment.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentRemoveApiView(APIView):
    
    serializer_class = CommentRemoveSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):

        try:
            comment = Comment.objects.get(pk=pk, author=request.user.id)
            serializer = self.serializer_class(comment, data=request.data)
            comment.delete()
            # return Response(serializer.data, status=status.HTTP_200_OK)

        except Comment.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)





class CommentApproveApiView(APIView):

    serializer_class = CommentApproveSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, pk, *args, **kwargs):

        try:
            pass





        except Comment.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AboutUsApiView(APIView):

    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        about = AboutUs.objects.all()
        serializer = self.serializer_class(about, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


















        