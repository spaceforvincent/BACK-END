from django import forms
from .models import Article


class ArticleForm (forms.ModelForm):

    class Meta :
        model = Article
        fields = '__all__'



# class ArticleForm(forms.Form):

#     REGION_A = 'gm'
#     REGION_B = 'bu'
#     REGION_C = 'sl'

#     REGION_CHOICES = [
#     (REGION_A,'구미'),
#     (REGION_B,'부울경'),
#     (REGION_C,'서울'),

#     ]

#     title = forms.CharField(max_length = 10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(widget=forms.Select, choices=REGION_CHOICES)
