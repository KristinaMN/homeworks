from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now()
    msg = f'Текущее время: {current_time.hour}:{current_time.minute}'
    return HttpResponse(msg)


def workdir_view(request):
    template = "app/work_dir.html"
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    path = os.getcwd()
    list_dir = os.listdir(path)
    return render(request, template, context={"list_dir": list_dir})
