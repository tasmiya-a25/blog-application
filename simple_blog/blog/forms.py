from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Comment form - TEAM MEMBER 3 RESPONSIBILITY Pratiksha"""
    
    class Meta:
        model = Comment
        fields = ['author', 'email', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email (optional)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment...'
            }),
        }
