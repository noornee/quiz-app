from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Course, Result
from quiz_questions.models import Question, Answer
# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'quiz_app/index.html'
    context_object_name = 'course_list'

class CourseDetailView(DetailView):
    model = Question
    template_name = 'quiz_app/quiz_detail.html'
    context_object_name = 'course_detail'

def course_data_view(request, pk):
    course = Course.objects.get(pk=pk)    
    questions = []
    for quest in course.get_questions():
        answers = []
        for ans in quest.get_answers():
            answers.append(ans.answer_text)
        questions.append({quest.question_text: answers })   
    return JsonResponse({
        'data': questions,
        'time': course.duration
    })  

