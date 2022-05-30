from rest_framework.serializers import ModelSerializer


from blog.models import Post, Comment, AboutUs


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class PostEditSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'





class PostDraftListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class AddCommentToPostSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'





class CommentRemoveSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        




class CommentApproveSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'





class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'





class PostPublishSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

