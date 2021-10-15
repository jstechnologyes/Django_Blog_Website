from django import forms
from .models import Post, Category, Comment

# choices=[('coding','coding'),('sports','sports'),('entartaiment','entartaiment'),]
choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author', 'category','body','snippet','header_image')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author','body','snippet')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

