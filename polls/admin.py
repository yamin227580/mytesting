from django.contrib import admin
from .models import *

# Register your models here.
class QAdmin(admin.ModelAdmin):
	list_display = ['question_text','pub_date']
admin.site.register(Question,QAdmin)

class CAdmin(admin.ModelAdmin):
	list_display = ['question','choice_text','votes']
admin.site.register(Choice,CAdmin)