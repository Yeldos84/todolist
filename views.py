from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from .models import TodoUsers
from .forms import TodoUsersForm
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def todo(request):
    return HttpResponse('ToDo APPS')


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

def notfound(request):
    return render(request, 'todolist/404.html')
class TodoUserView(CreateView):
    model = TodoUsers
    fields = '__all__'
    template_name = 'todolist/index.html'
    success_url = '/todolist/succes'


class TodoLoginView(FormView):
    model = TodoUsers
    template_name = 'todolist/succes.html'
    form_class = TodoUsersForm
    # success_url = '/todolist/succes_login'
    extra_context = {'login': TodoUsers.objects.all().last}


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




