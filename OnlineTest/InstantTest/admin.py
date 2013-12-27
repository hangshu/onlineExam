from django.contrib import admin
from models import Paper,Test,Subject,KnowledgePoint,Question,PaperQuestion

admin.site.register(Paper)
admin.site.register(Test)
admin.site.register(Subject)
admin.site.register(KnowledgePoint)
admin.site.register(Question)
admin.site.register(PaperQuestion)