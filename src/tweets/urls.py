from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import TweetDetailView, TweetListView

urlpatterns = [
    path('', TweetListView.as_view(),name='list'),
    path('1/', TweetDetailView.as_view(),name='detail'),
]
