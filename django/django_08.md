# API



### HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  - informational responses (1xx)
  - Successful responses (2xx)
  - Redirection messages (3xx)
  - Client error responses (4xx)
  - Server error responses (5xx)



### URI

- Uniform resource identifier

  - 통합 자원 식별자

  - 인터넷의 자원을 식별하는 유일한 주소

  - 인터넷에서 자원을 식별하거나 이름을 지정하는 데 사용되는 간단한 문자열

  - 하위개념

    - URL, URN

    - 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함



### API

- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 프로그래밍으로 소통
- WEB API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  - 현재 웹 개발은 모든 것을 직접 개발하기보다 여러 Open API를 활용하는 추세
- 응답 데이터 타입
  - HTML, XML, JSON 등



### REST

- REpresentational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계방법론
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리를 따르는 시스템을 RESTful이란 용어로 지칭함
- 자원과 주소의 지정 방법
  - 자원(정보) : URI
  - 행위 : HTTP Method (get, post, delete, put)
  - 표현 : json (javascript의 표기법을 따른 단순 문자열)

- Build RESTful API

|             | GET         | POST    | PUT         | DELETE      |
| ----------- | ----------- | ------- | ----------- | ----------- |
| articles/   | 전체글 조회 | 글 작성 |             |             |
| articles/1/ | 1번 글 조회 |         | 1번 글 수정 | 1번 글 삭제 |



### Serialization

- 직렬화
- Queryset 및 Model Instance와 같은 복잡한 데이터를 json, xml 등의 유형으로 쉽게 변환할 수 있는 python 데이터 타입으로 만들어줌
- django의 내장 HttpResponse를 활용한 json 응답 객체
- 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어줄 필요 없음

- Django REST Framework의 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

- ModelSerializer : 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
- many : Serializing multiple objects. 단일 인스턴스 대신 QuerySet 등을 직렬화

### Django ModelForm vs DRF Serializer

|          | Django    | DRF        |
| -------- | --------- | ---------- |
| Response | HTML      | JSON       |
| Model    | ModelForm | Serializer |



### api_view decorator

- view함수가 응답해야하는 HTTP 메서드의 목록을 리스트의 인자로 받음
- DRF에서는 선택이 아닌 필수적으로 작성해야 해당 view 함수가 정상적으로 동작함



### DRF with 1:N Relation

- Article 생성과 달리 Comment 생성은 생성 시에 참조하는 모델의 객체 정보가 필요
  - serializer.save(article=article)

- Read Only Field
  - 직렬화하지 않고 반환값에만 해당 필드가 포함되도록 설정할 수 있음
- PrimaryKeyRelatedField
- Nested relationships
  - 모델 관계상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩될 수 있음