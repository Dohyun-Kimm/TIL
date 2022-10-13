from tkinter import CASCADE
from django.db  import models
# 1
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번의사 {self.name}'

# N
class Patient(models.Model):
    name = models.TextField()
    # 참조한 테이블의 값은 int 로 저장 된다 두개 이상을 참조할 경우 데이터 타입이 튜플이 되기 때문에 불가능하다
    # -> M:N이 필요한 이유
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor.pk} {self.patient.pk}'


class Person(models.Model):
    friends = models.ManyToManyField('self', related_name ='people')
    
