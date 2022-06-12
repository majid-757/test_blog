from django.db import models
from django.conf import settings
from django.utils import timezone





class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


    



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def approve(self):
        self.approved_comment = True
        self.save()


    def __str__(self):
        return self.text


    
class AboutUs(models.Model):

    about_us = models.TextField(null=True, blank=True)    


    def __str__(self):
        return self.about_us



class PostView(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_view')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='myvisit')





class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)


    