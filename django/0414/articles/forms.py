from random import choices
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    pick_a = 'BLUE'
    pick_b = 'RED'
    pick_choice = {
        pick_a : 'blue',
        pick_b : 'red'
    }
    pick = forms.ChoiceField(choices=pick_choice, widget = forms.Select())
    class Meta:
        model = Comment
        fields = '__all__'