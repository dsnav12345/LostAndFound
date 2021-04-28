from django.forms import ModelForm
from django import forms
from .models import Post
from .models import ImageSearchModel

class ImageSearchForm(ModelForm):
    class Meta:
        model = ImageSearchModel
        fields ="__all__"

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=[
            'name',
            'place',
            'date',
            'time',
            'category',
            'image',
            'description',
        ]
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'time': forms.TimeInput(format='%H:%M')
        }
