from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Tweet
# Create your views here.

#RETRIEVE

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args,**kwargs)
        #context["another_list"] = 1
        #print(context)
        return context

# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request,"tweets/detail_view.html",context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     context = {
#         "object_list": queryset
#     }
#     return render(request,"tweets/list_view.html",context)
