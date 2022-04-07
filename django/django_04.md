## Django Form Class

- Form : Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML forms 생성
  - 클라이언트로 받은 데이터 수신 및 처리

- Form 선언하기

  ```django
  # articles/forms.py
  
  from django import forms
  
  class ArticleForm(forms.Form):
  	title = forms.CharField(max_length=10)
  	content = forms.CharField()
  
  # articles/views.py
  from .forms import ArticleForm
  def new(request):
  	form = ArticleForm()
  	context = {
  	'form' : form
  }
  	return render(request, 'articles/new.html', context)
  
  # new.html
  {% extends 'base.html' %}
  {% block content %}
    <h1>NEW</h1>
    <hr>
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {{form.as_p}}
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">back</a>
  {% endblock content %}
  ```

- rendering options (출력 옵션)
  - as_p() : 각 필드가 단락(p 태그)으로 감싸져서 렌더링됨
  - as_ul() : 각 필드가 목록 항목으로 감싸져서 렌더링 됨. <ul> 태그는 직접 작성해야 함
  - as_table() : 각 필드가 테이블 행으로 감싸져서 렌더링 됨. <table> 태그는 직접 작성해야 함.

- Django의 HTML input 요소 표현 방법

  - Form fields
    - input에 대한 <u>유효성 검사 로직</u>을 처리하며 템플릿에서 직접 사용됨
  - Widgets
    - <u>웹 페이지의 html input 요소 렌더링</u>
    - GET/POST 딕셔너리에서 데이터 추출
    - widgets은 반드시 Form fields에 할당됨

  ```
  # articles/forms.py
  
  from django import forms
  
  class ArticleForm(forms.Form):
  	title = forms.CharField(max_length=10)
  	content = forms.CharField(widget=forms.Textarea)
  ```

  ```python
  
  class ArticleForm(forms.Form):
  
      REGION_A = 'gm'
      REGION_B = 'bu'
      REGION_C = 'sl'
  
      REGION_CHOICES = [
      (REGION_A,'구미'),
      (REGION_B,'부울경'),
      (REGION_C,'서울'),
  
      ]
  
      title = forms.CharField(max_length = 10)
      content = forms.CharField(widget=forms.Textarea)
      region = forms.ChoiceField(widget=forms.Select, choices=REGION_CHOICES)
  ```

  

## ModelForm

- Model을 통해 Form Class를 만들 수 있음

  ```
  from django import forms
  from .models import Article
  
  
  class ArticleForm (forms.ModelForm):
  
      class Meta :
          model = Article
          fields = '__all__'
          # exclude = ['title', ]
  ```

  - 정의한 클래스 안에 Meta클래스를 선언하고, 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
    - fields와 exclude는 동시에 사용할 수 없음

```django
def create(request):
    if request.method == 'POST': #저장
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles.detail', article.pk)
    else:
        form = ArticleForm() #글쓰기 폼
    context = {
            'form': form
        }
    return render('articles/create.html', article.pk)
    #new의 view함수, url path 삭제 (create랑 하나로 합쳐줬기 때문에)
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' : #수정
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles.detail', article.pk)
    else:
        form = ArticleForm(instance=article) #수정 폼
    context = {
        'form' : form
    }
    return render(request, 'articles/update.html', context)
	#edit의 view 함수, url path 삭제 (update랑 하나로 합쳐졌기 때문에)
```



- is_valid() : 유효성 검사를 실행하고 데이터가 유효한지 여부를 boolean으로 반환

- save() : Form에 바인딩된 데이터에서 데이터베이스 객체를 만들고 저장

  - ModelForm의 하위 클래스는 기존 모델 인스턴스를 키워드 인자 instance로 받아들일 수 있음

    - instance 제공 : save()는 해당 인스턴스를 수정 (update)
    - instance 미제공 : save()는 지정된 모델의 새 인스턴스를 만듦 (create)

    ```
    form = ArticleForm(request.POST)
    
    #CREATE
    new_article = form.save()
    
    #UPDATE
    article = Article.objects.get(pk=1)
    form = ArticleForm(request.POST, instance=article)
    form.save()
    ```

    

  - Form의 유효성이 확인되지 않은 경우 save()를 호출하면 form.errors를 확인하여 에러 확인 가능



- Widget 권장 작성 방식

  ```django
  # articles/forms.py
  
  class ArticleForm(forms.ModelForm):
  	title = forms.CharField(
  	label='제목',
  	widget=forms.TextInput(
  	attrs={
  	'class': 'my-title',
  	'placeholder': 'Enter the title',
  	}
  	),
  	)
  
  	content = forms.CharField(
  	label='내용',
  	widget=forms.Textarea(
  	attrs={
  	'class': 'my-content',
  	'placeholder': 'Enter the content',
  	'rows : 5',
  	'cols' : 50,
  	}
  	),
  	error_messages={
  	'required': 'Please enter your content'
  	}
  )
  	
  	class Meta:
  	model = Article
  	fields = '__all__'
  ```

  
