from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import UserRegisterForm, UserLoginView,UserProfileView, UserPasswordChangeView, UserPasswordResetDoneView,UpdateUserProfileView,CreateUserProfileView #user_profile_view

app_name = 'users'



urlpatterns = [
    path('register/',UserRegisterForm.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('profile/create/',CreateUserProfileView.as_view(),name='create-profile'), 
    path('profile/update/<int:pk>/',UpdateUserProfileView.as_view(),name='update-profile'), 
    path('change-password/',UserPasswordChangeView.as_view(),name='password-change'),
    path('change-password/done/',UserPasswordResetDoneView.as_view(),name='password-reset-done')
]