from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Point(models.Model):
    point = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.point

        
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.IntegerField(default=0)
    point = models.ManyToManyField(Point)
    def __unicode__(self):
        return self.question
    def knowledge_points(self):
        return ', '.join([a.point for a in self.point.all()])
    knowledge_points.short_description = "Knowledge Point"

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length = 200)
    def __unicode__(self):
       return self.choice

class Paper(models.Model):
    questions = models.ManyToManyField(Question)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Test(models.Model):
    paper = models.ForeignKey(Paper)
    grade = models.IntegerField(default = 0)
    student = models.ForeignKey(User)
    def __studentName(self):
        return student.username
    #dueDate =models.DateTimeField('date overdue')
    def __unicode__(self):
        return self.paper.name



