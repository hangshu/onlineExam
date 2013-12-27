from django.db import models

# the best method is to inherit the class User, but no time to learn it. Probably next time!
class Student(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    
class Paper(models.Model):
    #paper_id = models.IntegerField(unique=True, primary_key=True)
    paper_name = models.CharField(max_length=50, unique=True)
    deadline = models.DateTimeField()
    duration = models.IntegerField() #number of minutes
    question_sum = models.IntegerField()
    #test_sum = models.IntegerField()

# for every student
class Test(models.Model):
    #test_id = models.IntegerField(unique=True, primary_key=True)
    student_id = models.ForeignKey(Student)
    paper_id = models.ForeignKey(Paper)
    grades = models.IntegerField()

class Subject(models.Model):
    #subject_id = models.IntegerField(unique=True, primary_key=True)
    subject_name = models.CharField(max_length=50)

class KnowledgePoint(models.Model):
    #kp_id = models.IntegerField(unique=True, primary_key=True)
    kp_name = models.CharField(max_length=10)
        
class Question(models.Model):
    #question_id = models.IntegerField(unique=True, primary_key=True)
    ANSWER_CHOICES = (
    (0, 'choiceA'),
    (1, 'choiceB'),
    (2, 'choiceC'),
    (3, 'choiceD'),
    )    
    kp_id = models.ForeignKey(KnowledgePoint)
    content = models.CharField(max_length=255)
    choiceA = models.CharField(max_length=200)
    choiceB = models.CharField(max_length=200)
    choiceC = models.CharField(max_length=200)
    choiceD = models.CharField(max_length=200)
    answer = models.IntegerField(choices=ANSWER_CHOICES) #1,2,3,4

class PaperQuestion(models.Model):
    p_id = models.ForeignKey(Paper)
    q_id = models.ForeignKey(Question)
 

