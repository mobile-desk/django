from django.contrib import admin
from .models import Video, Comment, Tag, Profile, Category, Contact

# Register your models here.
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)