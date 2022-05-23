from rest_framework.serializers import ModelSerializer


from blog.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text')




class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'









        