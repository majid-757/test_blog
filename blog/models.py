from django.db import models
from django.conf import settings
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
# from django.utils.encoding import python_2_unicode_compatible




class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # slug = models.SlugField(unique=True, max_length=100)
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    # blog_views=models.IntegerField(default=0)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)



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


