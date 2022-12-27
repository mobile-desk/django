from django.contrib import admin
from django.urls import path, include
from mysite import settings
from . import views
from .views import Hometube, viewtube, Update, Add, Complaint, CreateProfile, Delete, AddCategory, CategoryView, CategoryListView, LikeView, AddCommentView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.Hometube.as_view(), name="home"),
    #path('', hometube.as_view(), name="home"),
    path('upload/', Add.as_view(), name="upload"),
    path('complaint', Complaint.as_view(), name="complaint"),
    path('create-profile', CreateProfile.as_view(), name="create_profile"),
    path('upload/category/', AddCategory.as_view(), name="upload_category"),
    #the cats can be anything, just insure its the same name in your views.py
    path('category/<str:cats>/', CategoryView, name='category'), 
    path('category-list/', CategoryListView, name='category-list'), 
    path('author/<str:author_name>/', views.author_view, name='author'),
    path('signup', views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    path('viewtube/<int:pk>', viewtube.as_view(), name="viewtube"),
    

    path('viewtube/<int:pk>/comment', AddCommentView.as_view(), name="add-comment"),
    

    path('viewtube/edit/<int:pk>', Update.as_view(), name="update"),

    path('updateprofile', views.update_profile, name="updateprofile"),

    path('viewtube/<int:pk>/delete', Delete.as_view(), name="delete"),
    path('like/<int:pk>', LikeView, name='like_video'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('profile', views.view_user_posts, name='profile'),
    path('change-password/', views.change_password, name='change_password'),

]


urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)