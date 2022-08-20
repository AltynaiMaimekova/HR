from django.db import models
from django.utils import timezone


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        age = timezone.now().year - self.birth_date.unique_for_year
        return age


class Employee(AbstractPerson):
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    work_experience = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f'{self.name} born in {self.birth_date} works as {self.position} with {self.salary} since {self.work_experience}')
        super().save(*args, **kwargs)


class Passport(models.Model):
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=9)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self):
        if str(self.inn)[0] == 1:
            return 'female'
        else:
            return 'male'

    def __str__(self):
        return self.inn

    def save(self, *args, **kwargs):
        print(f'{self.employee} with {self.inn} with {self.id_card}')
        super().save(*args, **kwargs)


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50)
    members = models.ManyToManyField(Employee, through='Membership')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        print(f'{self.project_name}')
        super().save(*args, **kwargs)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.employee} joined {self.work_project} at {self.date_joined}'

    def save(self, *args, **kwargs):
        print(f'{self.employee} joined {self.work_project} in {self.date_joined}')
        super().save(*args, **kwargs)


class Client(AbstractPerson):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f'{self.name} born at {self.birth_date} living in {self.address} with phone {self.phone_number}')
        super().save(*args, **kwargs)


class VIPClient(Client):
    vip_status_start = models.DateField(default=timezone.now)
    donation_amount = models.IntegerField()

    def __str__(self):
        return f'{self.name} gave {self.donation_amount}'

    def save(self, *args, **kwargs):
        print(f'{self.name} born at {self.birth_date} living in {self.address} with phone {self.phone_number} recieved VIP in {self.vip_status_start} and provided {self.donation_amount}')
        super().save(*args, **kwargs)









