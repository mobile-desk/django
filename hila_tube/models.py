from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='images/profile/', default="images/default.png", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.CharField( max_length=500)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    complaint = models.TextField()
    image = models.ImageField(upload_to ='images/complaint/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title + '|' + str(self.user) + '|' + str(self.created_at)



class Video(models.Model):
    # other model fields here
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to ='images/thumbnail/', default="thumb.png", null=True, blank=True)
    video_file = models.FileField(upload_to='images/videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_videos')
    comments = models.ManyToManyField('Comment', blank=True)


    #tags = models.ManyToManyField('Tag', blank=True)

    def total_likes(self):
        return self.likes.count()



    def get_absolute_url(self):
        return reverse('viewtube',kwargs={'pk':self.pk})
#
    #def has_user_liked_or_subscribed(self, user: User) -> bool:
    #    likes = self.likes.filter(user=user)
    #    subscriptions = self.subscriptions.filter(user=user)
    #    return likes.exists() or subscriptions.exists()

    def __str__(self):
        return self.name + '|' + str(self.author) + '|' + str(self.created_at)




class Comment(models.Model):
    # Fields for the comment model
    videopost = models.ForeignKey(Video, related_name="video_comments", on_delete=models.CASCADE)
    body = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s' % (self.videopost.name, self.commenter, self.created_at)

    def get_absolute_url(self):
        return reverse('viewtube',kwargs={'pk':self.videopost.pk})




class Tag(models.Model):
    # Fields for the tag model
    videopost = models.ForeignKey(Video, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)