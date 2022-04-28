from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    PICK_A = False
    PICK_B = True
    PICKS = [
        (PICK_A, 'BLUE'),
        (PICK_B, 'RED'),
    ]
    # 둘 중에 하나만 고르는거니까..라디오버튼도 가능합니다.
    # pick = forms.ChoiceField(choices=PICKS, widget=forms.RadioSelect())
    pick = forms.ChoiceField(choices=PICKS)
    
    class Meta:
        model = Comment
        fields = ['pick', 'content']