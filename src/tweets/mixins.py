from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            form.add_error(None,ErrorList(["User must be logged in to continue"]))
            return self.form_invalid(form)

class UserOwnerMixin(FormUserNeededMixin,object):

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super().form_valid(form)
        else:
            form.add_error(None,ErrorList(["This use is not allowed to update this tweet"]))
            return self.form_invalid(form)
