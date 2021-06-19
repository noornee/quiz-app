from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView,PasswordResetDoneView
from .models import Result, Profile
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .custom_form import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
# from django.views.generic import CreateView



# Create your views here.

class UserRegisterForm(SuccessMessageMixin, FormView):
    template_name = 'users/register.html'
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
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('quiz:course-list')


class UserProfileView(LoginRequiredMixin, ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'users/profile.html'
    ordering = ['-mod_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.filter(user=self.request.user)
        context['profile_model'] = Profile.objects.filter(user=self.request.user)
        return context

class UpdateUserProfileView(UpdateView):
    model = Profile 
    # context_object_name = 'update-profile'
    template_name = 'users/update_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('users:profile')



class UserPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password-reset-done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'          