from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    #질문 목록 출력
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    #질문작성
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:detail', question.pk)
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    #상세 페이지
    # annotate
    comment_form = CommentForm()
    
    #비율 표시를 위해서 총개수, True개수, False 개수가 필요
    #역참조를 통해 각각 조회
    question = get_object_or_404(Question,pk=question_pk)
    total_count = question.comment_set.count()
    count_a = question.comment_set.filter(pick=0).count()
    count_b = question.comment_set.filter(pick=1).count()



    # annotate() 를 이용해서 조회
    
    #annoate : QuerySet 각 객체별 주석을 다는것과 같음...주석은 평균, 합계, 등이 될 수 있음
    # 아래는 주석을 달기 위한 기준선언, 우리는 객체별 총 댓글개수, TRUE 선택 개수, False 선택개수가 필요함
    # Count 클래스 참고 이외에도 AVG, MAX, MIN 등의 통계를 작성할 수 있음 Django_aggregation.md 문서 참조
    # https://docs.djangoproject.com/en/4.0/topics/db/aggregation/#cheat-sheet
    total_count = Count('comment')
    count_a = Count('comment', filter=Q(comment__pick=0))
    count_b = Count('comment', filter=Q(comment__pick=1))
    # 객체별로 주석을 달아서 결과를 반환받음
    result = Question.objects.annotate(
                            total_count=total_count,
                            count_a=count_a,
                            count_b=count_b
                        )
    # 결과 안에서 우리가 URI로 받은 question_pk와 같은 question 객체를 얻어옴 : 댓글개수 와 종류별 댓글 개수를 포함
    #get_object_or_404() 메서드는 첫 번째 인자로 (클래스|매니저|QuerySet) 을 받는다. 
    # 53번 줄의 결과는 QuerySet 이므로 첫번째 인자로 들어갈 수 있다. 결과내 재검색.
    question = get_object_or_404(result, pk=question_pk)
    comments = question.comment_set.order_by('-pk') # 내림차순정렬
    #각 선택별 비율 계산
    a_per = round(question.count_a / question.total_count * 100, 2) if question.total_count else 0
    b_per = round(question.count_b / question.total_count * 100, 2) if question.total_count else 0


    #detail 페이지를 표현하기 위한 데이터
    # 질문, 댓글들, 댓글 작성을 위한 폼, 선택지 선택 비율
    context = {
        'question': question,
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per,
        'b_per': b_per,
    }

    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)


def random(request):
    # 1. order_by('?')
    # question = get_object_or_404(Question.objects.order_by('?')[:1])
    
    # 2. annotate를 사용하지 않는 버전 
    import random

    pk_list = []
    for value in Question.objects.values('pk'):
        pk_list.append(value['pk'])
    question = get_object_or_404(Question, pk=random.choice(pk_list))

    count_a = len(question.comment_set.filter(pick=0))
    count_b = len(question.comment_set.filter(pick=1))
    total_count = count_a + count_b

    comment_form = CommentForm()
    comments = question.comment_set.order_by('-pk')

    if total_count == 0:
        a_per = 0
        b_per = 0
    else:
        a_per = round(count_a / total_count * 100, 2)
        b_per = round(count_b / total_count * 100, 2)
    
    context = {
        'question': question, 
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per, 
        'b_per': b_per,
    }

    return render(request, 'eithers/detail.html', context)