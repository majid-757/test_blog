from django.urls import path


from .views import PostDeleteApiView, PostListApiView

urlpatterns = [
    path('list/', PostListApiView.as_view(),name='post-list'),
    # path('<int:pk>', PostDetailApiView.as_view(), name='post-detail'),
    path('<int:pk>', PostDeleteApiView.as_view(), name='post-delete'),
]







