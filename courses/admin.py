from django.contrib import admin

from .models import Professor, Course


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'professor']
    list_filter = ['created', 'professor']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
