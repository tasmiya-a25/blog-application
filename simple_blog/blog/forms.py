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
                'placeholder': 'Your name *',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email (optional)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment... *',
                'required': True
            }),
        }
        labels = {
            'author': 'Name',
            'email': 'Email address',
            'content': 'Comment'
        }
        help_texts = {
            'email': 'Won\'t be published.',
            'content': 'Be respectful and kind.'
        }

    def clean_content(self):
        """Ensure comment has meaningful content."""
        content = self.cleaned_data['content'].strip()
        if len(content) < 10:
            raise forms.ValidationError('Comment must be at least 10 characters long.')
        return content

    def clean(self):
        """Additional form-wide cleaning."""
        cleaned_data = super().clean()
        author = cleaned_data.get('author', '').strip()
        if len(author) < 2:
            raise forms.ValidationError('Name must be at least 2 characters.')
        return cleaned_data
