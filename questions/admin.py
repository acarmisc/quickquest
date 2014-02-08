from django.contrib import admin
from questions.models import Question, Question_type, Question_level, Answer

admin.site.register(Question)
admin.site.register(Question_type)
admin.site.register(Question_level)
admin.site.register(Answer)
