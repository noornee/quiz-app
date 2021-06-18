from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Course, Result
from quiz_questions.models import Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'quiz_app/index.html'
    context_object_name = 'course_list'



def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request,'quiz_app/quiz_detail.html',{
        'obj': course
    })


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

def save_data_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for key in data_.keys():
            question = Question.objects.get(question_text=key)
            questions.append(question)

        user = request.user
        course = Course.objects.get(pk=pk)

        score = 0
        multiplier = 100 / course.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.question_text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for answer in question_answers:
                    if a_selected == answer.answer_text:
                        if answer.correct:
                            score += 1
                            correct_answer = answer.answer_text
                    else:
                        if answer.correct:
                            correct_answer = answer.answer_text       

                results.append({q.question_text: {'correct_answer': correct_answer, 'answered': a_selected} })
            else:
                results.append({q.question_text: 'not answered','correct_answer': correct_answer, })
        score_ = score * multiplier    
        Result.objects.create(course=course, user=user, score=score_)    

        return JsonResponse({'score': score_, 'results': results})
