from django.shortcuts import render
import random
from .models import puls, PulsChoice
from .forms import TgForm, ChoiceForm, RegForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

# Create your views here.
# возвращает аштиэмель из функций

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        f = ChoiceForm(request.POST or None)
        print(f.data)
        f.Create_Form(f.data)
    welcome = ['welcome', 'hi', 'broh']
    context = {}
    allPuls = list(puls.objects.all())
    context['allPuls'] = allPuls
    #context['TgForm'] =  TgForm()
    context['ChoiceForm'] = ChoiceForm()
    return render(request, 'index.html', context)

def check(request):
    return render(request, 'help.html', {})

class LoginPage(LoginView):
    template_name = 'login.html'

class Register(CreateView):
    template_name = 'reg.html'
    form_class = UserCreationForm
    success_url = 'login'