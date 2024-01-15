# Register your models here.
from django import forms
from .models import Video,HomeVideo

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'file']
        
        
class HomeVideoForm(forms.ModelForm):
    class Meta:
        model = HomeVideo
        fields = ['title', 'description', 'file']