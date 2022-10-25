from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя пользователя', max_length = 100)
    mail = models.CharField('Почта', max_length = 200)
    #tel = models.CharField('Телефон', max_length = 100)
    status = models.CharField('Статус', max_length = 100)
    #department = models.CharField('Департамент', max_length = 200)
    #positions = models.CharField('Должность', max_length = 200)

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    message = models.TextField('Текст сообщения') 

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'