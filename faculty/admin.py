from django.contrib import admin
from faculty.models import Department, Discipline, Program, Teacher, FacultyInfo


# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "degree", "department"]


admin.site.register(Department)
admin.site.register(Discipline)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(FacultyInfo)
