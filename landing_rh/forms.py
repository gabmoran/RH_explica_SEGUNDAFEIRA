# -*- coding: utf-8 -*-
from django import forms
from landing_rh.models import Newsletter

class NewsletterForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)