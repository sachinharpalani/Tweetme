from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tweet
from .form import TweetModelForm
from .mixins import FormUserNeededMixin,UserOwnerMixin

# Create your views here.

#CREATE

class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    template_name = 'tweets/create_view.html'
    form_class = TweetModelForm
    login_url = '/admin/'


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {"form" : form}
#     return render(request,'tweets/create_view.html',context)

#RETRIEVE

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    #This is optional if used another key name apart from pk. If used pk django automatically retrieved pk object
    # def get_object(self):
    #     print(self.kwargs)
    #     id = self.kwargs.get("id")
    #     return Tweet.objects.get(id=id)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args,**kwargs)
        #context["another_list"] = 1
        #print(context)
        return context

# def tweet_detail_view(request, id=1):
#     obj = tweet.objects.get(id=id)

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

#UPDATE

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'

#DELETE

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tweets/delete_confirm.html'
    model = Tweet
    success_url = reverse_lazy("tweets:list")
