from django.contrib import admin
from .models import Student, Module
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','age','email')
    search_fields = ('firstName','lastName','email')
    list_filter = ('age','modules')
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code','name')
