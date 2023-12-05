import requests
from django.forms import ModelForm
from django import forms
from .models import puls, PulsChoice
from crispy_forms.helper import FormHelper
import json

class ChoiceForm(forms.Form):
    title = forms.CharField(label='Puls title', max_length=255)
    description = forms.CharField(label='description', widget=forms.Textarea)
    firstChoice = forms.CharField(label='First choice', max_length=100)
    secChoice = forms.CharField(label='Second choice', max_length=100)

    def Create_Form(self, data):
        puls_obj= puls()
        puls_obj.title = data['title']
        puls_obj.description = data['description']
        
        fc = PulsChoice()
        fc.value = data['firstChoice']
        fc.save()
        
        sc = PulsChoice()
        sc.value = data['secChoice']
        sc.save()

        puls_obj.fchoice = fc
        puls_obj.schoice = sc

        puls_obj.save()


class TgForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(label='description', widget=forms.Textarea)
    
    def Send(self, data):
        token = '6306105011:AAHW09CeRuAEzWZAyBoirMGdgvE7PcIhqFQ'
        chat = '1473386210'
        msg = f'title: {data['title']}, description: {data['description']}'

        url = f'https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={chat}'

        response = requests.post(url, data=msg)

        
class RegForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    password = forms.CharField(label='password',min_length=8)
    password_c = forms.CharField(label='repeat password', min_length=8)
    def pass_check(self, data):
        if password == password_c:
            return True
        else:
            return 'passwords dont match'
    