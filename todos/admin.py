from django.contrib import admin
from .models import Events

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('task','description','created_date','due_date','task_status',)

admin.site.register(Events,MemberAdmin)