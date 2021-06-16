from django.urls import path
from .views import CourseListView,course_detail_view, course_data_view, save_data_view

app_name = 'quiz'



urlpatterns = [
    path('',CourseListView.as_view(),name='course-list'),
    path('<int:pk>/',course_detail_view,name='course-detail'),
    path('<int:pk>/data/',course_data_view,name='course-data-view'),
    path('<int:pk>/save/',save_data_view,name='save-data-view'),

]