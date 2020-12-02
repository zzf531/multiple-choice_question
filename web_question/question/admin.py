from django.contrib import admin
from .models import questions

# Register your models here.
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'content', 'pic', 'options', 'answer', 'option_number')
    search_fields = ('number', )


admin.site.register(questions, QuestionModelAdmin)
