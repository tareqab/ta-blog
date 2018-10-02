from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)# to render this field as textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # To create a form from a model, we just need to indicate which model to use to build the form in the Meta class of the form.
        fields = ('name', 'email', 'body')