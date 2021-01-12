
from django.shortcuts import render

from .models import homework

def year_archive(request, year):
    a_list = homework.objects.filter(日期__year=year)
    context = {'year': year, 'homework_list': a_list}
    return render(request, 'news/year_archive.html', context)


from .models import 学生信息,homework
from django.views.generic.edit import CreateView


class homeworkCreate(CreateView):
    model = homework
    template_name = 'homework_form.html'
    fields = ['离校日期','目的地','交通工具','姓名','学号']