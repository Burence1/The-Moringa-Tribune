from django import forms
from django.forms import widgets
from .models import Article
from news import models

class NewsLetterForm(forms.Form):
  your_name=forms.CharField(label='First Name',max_length=30)
  email=forms.EmailField(label='Email')

class NewsArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    exclude = ['editor','pub_date']
    widgets = {
      'tags':forms.CheckboxSelectMultiple(),
    }