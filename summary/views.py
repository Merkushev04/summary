from django.shortcuts import render
from .models import *
from django.utils.safestring import mark_safe
import markdown
from .forms import MessageForm
from django.http import HttpResponseRedirect
import telepot

token = '1212716658:AAFMEBth1fyC-miiafHV8rSIRwNaMgMAGEE'
my_id = -440947889
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-440947889, text, parse_mode="Markdown")


def markdown_format(text):
    return mark_safe(markdown.markdown(text))


def base(request):
    intros = Intro.objects.all()
    contacts = Contact.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    works = Work.objects.all()
    courses = Courses.objects.all()
    projects = Project.objects.all()
    message = Message.objects.all()
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            company = form.cleaned_data['company']
            contact = form.cleaned_data['contact']
            message = form.cleaned_data['message']
            company_message = "*ПРЕДЛОЖЕНИЕ РАБОТЫ*:" + "\n" + "*КОМПАНИЯ*: " + str(company) + "\n" + "*КОНТАКТЫ*: " + str(contact) + "\n" + "*СООБЩЕНИЕ*: " + str(message)
            send_message(company_message)
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()

    return render(request, 'summary/base.html', {'intros': intros,
                                                 'contacts': contacts,
                                                 'educations': educations,
                                                 'skills': skills,
                                                 'works': works,
                                                 'courses': courses,
                                                 'projects': projects,
                                                 'form': form,
                                                 })
