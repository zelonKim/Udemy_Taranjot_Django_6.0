from .models import  Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }
        