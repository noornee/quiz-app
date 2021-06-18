from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from quiz_app.models import Result
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .custom_form import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class UserRegisterForm(SuccessMessageMixin, FormView):
    template_name = 'quiz_app/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('quiz:course-list')
    success_message = "your account was created successfully"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterForm, self).form_valid(form) 


class UserLoginView(LoginView):
    template_name = 'quiz_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('quiz:course-list')


class UserProfileView(LoginRequiredMixin, ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'quiz_app/profile.html'
    ordering = ['-mod_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.filter(user=self.request.user)
        return context