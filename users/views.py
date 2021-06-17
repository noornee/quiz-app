from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from quiz_app.models import Result
from django.urls import reverse_lazy


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'quiz_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('quiz:course-list')

# def user_profile_view(request):
#     result = Result.objects.all()
#     return render(request, 'quiz_app/profile.html', {
#         'results': result
#     })

class UserProfileView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'quiz_app/profile.html'
    ordering = ['-mod_date']
