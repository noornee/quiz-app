from django.urls import path
from .views import CourseListView, CourseDetailView, course_data_view

app_name = 'quiz'



urlpatterns = [
    path('',CourseListView.as_view(),name='course-list'),
    path('<int:pk>/',CourseDetailView.as_view(),name='course-detail'),
    path('<int:pk>/data',course_data_view,name='course-data')
]