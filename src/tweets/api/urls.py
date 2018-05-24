from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .views import TweetListAPIView,TweetCreateAPIView

app_name ='tweets'

urlpatterns = [

    path('', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    path('create/', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
]
