from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.decorators import permission_required

from InstantTest.models import Question, Paper, PaperQuestion
from InstantTest.forms import SignInForm, AddQuestions, AddPaper

@csrf_exempt
def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:  
                login(request, user)
                return HttpResponseRedirect('/teacherhome/')
    else:
        form = SignInForm()
    return render_to_response('signin.html', {'form':form})

def sign_out(request):
    logout(request)
    return HttpResponseRedirect("/signin/")

@login_required
#@permission_required('add_questions', login_url="/signin/")
def index(request):
    msg = "welcome"
    return render_to_response('teacherhome.html', {'msg':msg})

@csrf_exempt
@login_required
def add_question(request):
    if request.method == "POST":
        form = AddQuestions(request.POST)
        if form.is_valid():
            form.save()
            msg = "save it successfully"
            return render_to_response('addquestion.html', {'msg':msg})
    else:
        form = AddQuestions()
    return render_to_response('addquestion.html', {'form':form})

@csrf_exempt
@login_required
def view_question(request):
    questions = Question.objects.all()
    return render_to_response('viewquestion.html', {'questions':questions})


@csrf_exempt
@login_required
def edit_question(request):
    temp1 = request.path
    temp2 = temp1.split('/')
    q = temp2[2]
    question = Question.objects.get(id = q)
    if request.method == "POST":
        form = AddQuestions(request.POST)
        if form.is_valid():
            form.update(question)
            msg = "edit it successfully"
            return render_to_response('editquestion.html', {'msg':msg})
    else:
        form = AddQuestions({'knowledge_point': question.kp_id.kp_name, 'content': question.content, \
                             'choiceA': question.choiceA, 'choiceB': question.choiceB,\
                             'choiceC': question.choiceC, 'choiceD': question.choiceD, 'answer': question.answer})
        return render_to_response('editquestion.html', {'form':form})

@csrf_exempt
@login_required
def delete_question(request):
    questions = Question.objects.all()
    if 'questions' in request.POST:
        questions = request.REQUEST.getlist('questions')
        if questions is not None:
            for question in questions:
                q = Question.objects.get(content = question)
                q.delete()
#             else:
#                 q = Question.objects.get(content = questions)
#                 q.delete()
            msg = 'delete successful'
        else:
            msg = 'no questions'
        return render_to_response('deletequestion.html', {'msg':msg})
    return render_to_response('deletequestion.html', {'questions':questions})

@csrf_exempt
@login_required  
def add_paper(request):
    if 'paper_name' in request.POST:
        addpaperform = AddPaper(request.POST)
        if addpaperform.is_valid():
            addpaperform.save()
            pname = addpaperform.cleaned_data['paper_name']
            questions = Question.objects.all()
            return render_to_response('addpaper.html',{'questions':questions, 'pname':pname})
    elif 'questions' in request.POST:
        questions = request.REQUEST.getlist('questions')
        if questions is not None:
            pname = request.POST['pname']
            pname = Paper.objects.get(paper_name=pname)
            for q in questions:
                q = Question.objects.get(content=q)
                p_q = PaperQuestion(p_id = pname,q_id = q)
                p_q.save()
            msg = 'the paper has relesed'
            return render_to_response('addpaper.html',{'msg':msg})
        else:
            msg = 'error!'
            return render_to_response('addpaper.html',{'msg':msg})
    else:
        addpaperform = AddPaper()
    return render_to_response('addpaper.html', {'addpaperform':addpaperform})    
