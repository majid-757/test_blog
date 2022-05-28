from django.urls import path


from .views import PostDeleteApiView, PostListApiView, PostCreateApiView, PostDetailApiView

urlpatterns = [
    path('list/', PostListApiView.as_view(),name='post-list'),
    path('create/', PostCreateApiView.as_view(), name='post-create'),
    path('detail/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
]







