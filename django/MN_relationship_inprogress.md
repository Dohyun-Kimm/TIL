# M:N relationship

 두개의 테이블이 서로  N:1관계를 가지고 연관되는 경우입니다.


 ## ManyToManyField

   다대다(M:N) 관계를 설정 할때 사용 하는 모델 필드. `ForeignField`의 복수형이라고 생각하면 편합니다.
 M:N 관계로 설정할 모델 클래스가 필수 인자로 필요합니다.
 `RelatedManager`를  사용해서 개체를 추가, 제거, 생성이 가능합니다. 

ex) `add()`, `remove()`, `create()`, `clear()`

### Arguments

1. **related_name:** 

   역참조를 위한 별명이라고 생각하면 이해하기 편합니다. 

   예를 들어, `Patient`라는 테이블에서 `Doctor`라는 테이블을 참조하기위해, `Patient`의 모델에 `ManyToManyField()`를 사용했다면,

   `Doctor`에서 `patient`를 참조할땐 `patient_set`을 써야 하지만, related_name을 `patients`라고 설정하면 `patient_set` 대신 `patients`를 사용하면 됩니다.



2.  **through** 

   중개 테이블을 직접 작성하는 경우, `through` 옵션을 사용하여 주개 테이블을 나타내는 모델을 지정할 수 있습니다. 

   일반적으로 중개 테이블에 추가 데이터를 사용하는 M:N관계와 연결하려는 경우에 사용됩니다.

   중개 테이블: 서로 참조하는 두 테이블이 만들어내는 새로운 데이터를 담는 테이블.



3. **symmetrical**

   기본 값: True

   `ManyToManyField`가 자기 자신을 가리키는 정의에만 사용합니다. 

   역참조 매니저 `_set`을 추가하지 않습니다.

   

## Related Manager



# M:N 구현하기

1. model 관계 설정하기

   `models.py` 에 `ManyToManyField` 작성하기. ( 참조 모델, related_name 설정하기)

   

2. Migration 진행하기

   모델에 변화가 생겼기 때문에 마이그래이션을 해주어야합니다.

   `python manage.py makemigrations`  --> `python manage.py migrate`

   

3. url 및 view 함수 작성하기
4.  데코레이터 작성하기