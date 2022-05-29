from django.urls import path


from .views import (
    PostDeleteApiView, 
    PostListApiView, 
    PostCreateApiView, 
    PostDetailApiView,
    PostEditApiView,
    PostDraftListApiView,
    AddCommentToPostApiView,
    CommentRemoveApiView,
    AboutUsApiView,

)

urlpatterns = [
    path('list/', PostListApiView.as_view(),name='post-list'),
    path('create/', PostCreateApiView.as_view(), name='post-create'),
    path('detail/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
    path('delete/<int:pk>/', PostDeleteApiView.as_view(), name='post-delete'),
    path('edit/<int:pk>/', PostEditApiView.as_view(), name='post-edit'),
    path('draft/', PostDraftListApiView.as_view(), name='post-draft'),
    path('add-comment-to-post/', AddCommentToPostApiView.as_view(), name='add-comment-to-post'),
    path('comment-remove/<int:pk>', CommentRemoveApiView.as_view(), name='comment-remove'),
    path('about/', AboutUsApiView.as_view(), name='about'),
]







