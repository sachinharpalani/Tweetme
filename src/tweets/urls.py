from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import TweetDetailView, TweetListView,TweetCreateView

urlpatterns = [
    path('', TweetListView.as_view(),name='list'),
    path('<int:pk>/', TweetDetailView.as_view(),name='detail'),
    path('create/', TweetCreateView.as_view(),name='create')
]
