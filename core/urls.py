from django.contrib import admin
from django.urls import path, include
from mysite import settings
from . import views
#from .views import blog, articleView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hila_tube.views import Hometube, signup, signin, signout



urlpatterns = [
    path('', views.home, name="home"),
    path('gallery', views.gallery, name="gallery"),
    path('hila_tube', Hometube.as_view(), name="hometube"),
    #path('hila_tube', hometube.as_view(), name="hometube"),
    path('signup', signup , name="signup"),
    path('signin', signin , name="signin"),
    path('signout', signout , name="signout"),
    #path('signup', views.signup , name="signup"),
    #path('signin', views.signin , name="signin"),
    #path('signout', views.signout , name="signout"),
    #path('article/<int:pk>', articleView.as_view(), name="article"),
]



urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)