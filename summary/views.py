from django.shortcuts import render
from .models import *


def base(request):
    intros = Intro.objects.all()
    contacts = Contact.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    works = Work.objects.all()
    courses = Courses.objects.all()
    projects = Project.objects.all()
    return render(request, 'summary/base.html', {'intros': intros,
                                                 'contacts': contacts,
                                                 'educations': educations,
                                                 'skills': skills,
                                                 'works': works,
                                                 'courses': courses,
                                                 'projects': projects,
                                                 })
