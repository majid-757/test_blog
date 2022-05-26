from django.urls import path


from .views import PostDetailApiView, PostDeleteApiView, PostListOrCreateApiView

urlpatterns = [
    path('create/', PostListOrCreateApiView.as_view(),name='post-create'),
    # path('<int:pk>', PostDetailApiView.as_view(), name='post-detail'),
    path('<int:pk>', PostDeleteApiView.as_view(), name='post-delete'),
]







