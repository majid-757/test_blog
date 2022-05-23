from django.urls import path


from .views import PostListApiView, PostDetailApiView, PostDeleteApiView

urlpatterns = [
    path('', PostListApiView.as_view(),name='post-list'),
    path('id/', PostDetailApiView.as_view(), name='post-detail'),
    path('delete/', PostDeleteApiView.as_view(), name='post-delete'),
]







