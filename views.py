from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from .models import TodoUsers, TodoModelCreate
from .forms import TodoUsersForm, SearchForm
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.contrib.auth.decorators import login_required

class TodoViewCreate(CreateView):
    model = TodoModelCreate
    fields = '__all__'
    template_name = 'todolist/home.html'
    success_url = '/todolist/'
    extra_context = {'add': TodoModelCreate.objects.all().last}



class TodoShow(ListView):
    model = TodoModelCreate
    template_name = 'todolist/show.html'
    extra_context = {
        'all': TodoModelCreate.objects.all()
    }


def tododelete(request):
    TodoModelCreate.objects.all().delete()
    return redirect(to='/todolist')



# def todo(request):
#     return HttpResponse('ToDo APPS')


def about(request):
    return HttpResponse('about page')


def info(request):
    return HttpResponse('info page')

def lang(request):
    return HttpResponse('lang page')


def contact(request):
    return HttpResponse(f'contact page')



def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    c = TodoUsers.objects.values('login')
    r = [q for q in c]
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(0, 500, str(r))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="logs.pdf")


"""DZ-11"""

def succes_login(request):
    # context = {'login': TodoUsers.objects.all().last}
    return render(request, 'todolist/succes_login.html')


def google(request):
    # context = {'login': TodoUsers.objects.all().last}
    return render(request, 'todolist/google.html')

def notfound(request):
    return render(request, 'todolist/404.html')


def render_base_template(request):
    return render(request, 'todolist/base.html')

def  render_navbar(request):
    return render(request, 'todolist/navbar.html')

def render_login_ok(request):
    return render(request, 'todolist/login_ok.html')

class TodoUserView(CreateView):
    model = TodoUsers
    fields = '__all__'
    template_name = 'todolist/index.html'
    success_url = '/todolist/succes'



class TodoShowAllUsers(CreateView):
    model = TodoUsers
    fields = '__all__'
    template_name = 'todolist/allusers.html'
    extra_context = {
        'allusers': TodoUsers.objects.all()
    }



def show_one_user(request, id):
    context = {'oneuser': TodoUsers.objects.get(id=id)}
    return render(request, 'todolist/oneusers.html', context)

# class TodoShowOnelUser(CreateView):
#     model = TodoUsers
#     fields = '__all__'
#     template_name = 'todolist/oneusers.html'
#     extra_context = {
#         'oneusers': TodoUsers.objects.all()
#     }


class TodoLoginView(FormView):
    model = TodoUsers
    template_name = 'todolist/succes.html'
    form_class = TodoUsersForm
    success_url = '/todolist/succes_login'
    extra_context = {'login': TodoUsers.objects.all().last}

class Captcha(FormView):
    model = TodoUsers
    form_class = TodoUsersForm
    template_name = 'todolist/index.html'
    success_url = '/todolist/succes'

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            # text_id = sf.cleaned_data['text_id'].pk
            bbs = list(TodoUsers.objects.filter(login__icontains=keyword))
            context = {'bbs':bbs, 'key':keyword}
            return render(request, 'todolist/search.html', context)
    else:
        sf = SearchForm()
        context = {'form':sf}
        return render(request, 'todolist/index.html', context)

    def form_valid(self, form):
        # print(type(form.cleaned_data['login']))
        # print(type(TodoUsers.objects.get(login=form.cleaned_data['login'])))
        # if form.cleaned_data['login'] == str(TodoUsers.objects.get(login=form.cleaned_data['login'])):
        #     return HttpResponse('ok')
        # elif form.cleaned_data['login'] is not str(TodoUsers.objects.get(login=form.cleaned_data['login'])):
        #     return JsonResponse(form.errors, status=400)
        try:
            if form.cleaned_data['login'] == str(TodoUsers.objects.get(login=form.cleaned_data['login'])):
                return HttpResponse('ok')
        except ObjectDoesNotExist:
            return redirect(to='/todolist/404')




