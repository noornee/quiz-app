from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import UserLoginView,UserProfileView #user_profile_view
from .views import CourseListView,course_detail_view, course_data_view, save_data_view

app_name = 'quiz'



urlpatterns = [
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='quiz:login'), name='logout'),
    # path('profile/',user_profile_view, name='profile'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('',CourseListView.as_view(),name='course-list'),
    path('<int:pk>/',course_detail_view,name='course-detail'),
    path('<int:pk>/data/',course_data_view,name='course-data-view'),
    path('<int:pk>/save/',save_data_view,name='save-data-view'),

]