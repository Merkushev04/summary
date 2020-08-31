from django.contrib import admin
from .models import *


@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ['position', 'intro', 'image', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'information']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['university', 'specialization', 'date_start', 'date_end',]


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['site', 'specialization', ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level',]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['place', 'position', 'duties', 'instruments', 'date_start', 'date_end',]
    list_filter = ['place', ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'link', ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['company', 'contact', 'message', ]
    list_filter = ['company', ]

