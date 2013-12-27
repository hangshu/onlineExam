from django import forms
from InstantTest.models import Question, KnowledgePoint, Paper
import re
import time, datetime

class SignInForm(forms.Form):
    username = forms.CharField(initial='admin')
    password = forms.CharField(widget=forms.PasswordInput())
    # need to mistakes warning here
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username is None or not re.search(r'^\w+$', username):
            raise forms.ValidationError('username is invalid')
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if password is None:
            raise forms.ValidationError('please input password')
    
class AddQuestions(forms.Form):
    knowledge_point = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea, max_length=500)
    choiceA = forms.CharField(widget=forms.Textarea, max_length=500)
    choiceB = forms.CharField(widget=forms.Textarea, max_length=200)
    choiceC = forms.CharField(widget=forms.Textarea, max_length=200)
    choiceD = forms.CharField(widget=forms.Textarea, max_length=200)
    answer = forms.IntegerField()
    
    def clean_all(self):
        knowledge_point = self.cleaned_data['knowledge_point']
        content = self.cleaned_data['content']
        choiceA = self.cleaned_data['choiceA']
        choiceB = self.cleaned_data['choiceB']
        choiceC = self.cleaned_data['choiceC']
        choiceD = self.cleaned_data['choiceD']
        answer = self.cleaned_data['answer']
        if knowledge_point is None:
            raise forms.ValidationError('please input knowledge point')
        if content is None:
            raise forms.ValidationError('please input the content')
        if choiceA is None:
            raise forms.ValidationError('please input the choice A')
        if choiceB is None:
            raise forms.ValidationError('please input the choice B')
        if choiceC is None:
            raise forms.ValidationError('please input the choice C')
        if choiceD is None:
            raise forms.ValidationError('please input the choice D')
        if answer is None:
            raise forms.ValidationError('please input answer point')
    
    def save(self):
        kp = self.cleaned_data['knowledge_point']
        content = self.cleaned_data['content']
        choiceA = self.cleaned_data['choiceA']
        choiceB = self.cleaned_data['choiceB']
        choiceC = self.cleaned_data['choiceC']
        choiceD = self.cleaned_data['choiceD']
        answer = self.cleaned_data['answer']
        try:
            kp_object = KnowledgePoint.objects.get(kp_name = kp)
        except KnowledgePoint.DoesNotExist:
            kp_object = KnowledgePoint(kp_name = kp)
            kp_object.save()
        q = Question(kp_id = kp_object, content = content, \
                      choiceA = choiceA, choiceB = choiceB, \
                      choiceC = choiceC, choiceD = choiceD, answer = answer)
        q.save()
    
    def update(self, question):
        kp = self.cleaned_data['knowledge_point']
        try:
            kp_object = KnowledgePoint.objects.get(kp_name = kp)
        except KnowledgePoint.DoesNotExist:
            kp_object = KnowledgePoint(kp_name = kp)
            kp_object.save()
        question.kp_id = kp_object
        question.content = self.cleaned_data['content']
        question.choiceA = self.cleaned_data['choiceA']
        question.choiceB = self.cleaned_data['choiceB']
        question.choiceC = self.cleaned_data['choiceC']
        question.choiceD = self.cleaned_data['choiceD']
        question.answer = self.cleaned_data['answer']
        question.save()

class AddPaper(forms.Form): 
    paper_name = forms.CharField(max_length=50)
    deadline = forms.DateTimeField()
    duration = forms.IntegerField()
    question_sum = forms.IntegerField()
    
    def clean_paper_name(self):
        paper_name = self.cleaned_data['paper_name']
        try:
            paper_name = Paper.objects.get(paper_name=paper_name)
        except Paper.DoesNotExist:
            return paper_name
        raise forms.ValidationError('Paper has already existed!')    
        
    def save(self):
        paper_name = self.cleaned_data['paper_name']
        deadline = self.cleaned_data['deadline']
        duration = self.cleaned_data['duration']
        question_sum = self.cleaned_data['question_sum']
        if len(Question.objects.all()) > question_sum:
            #handle the time format
            #deadline = time.strptime(deadline,'%Y-%m-%d %H:%M:%S')
            #deadline = datetime.datetime(deadline.tm_year, deadline.tm_mon, deadline.tm_mday, deadline.tm_hour, deadline.tm_min, deadline.tm_sec)
            p = Paper(paper_name=paper_name, deadline=deadline,\
                      duration=duration, question_sum=question_sum)
            p.save()
        else:
            raise forms.ValidationError('Too more questions')


class InitiateTest(forms.Form):
    student_id = forms.IntegerField()
    paper_name = forms.CharField(max_length=50)        
            
    
        