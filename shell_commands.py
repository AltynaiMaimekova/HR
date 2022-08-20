from employee.models import *

alex = Employee.objects.create(name='Alex', birth_date='2000-12-12',
                               position='sales manager', salary=500, work_experience='2021-12-12')

kuban = Employee.objects.create(name='Kuban', birth_date='1989-10-12',
                               position='product manager', salary=800, work_experience='2010-10-10')

victor = Employee.objects.create(name='Victor', birth_date='2000-12-12',
                               position='IT specialist', salary=700, work_experience='2019-11-11')

altynai = Employee.objects.create(name='Altynai', birth_date='1989-5-4',
                               position='data analyst', salary=900, work_experience='2022-5-12')

passport1 = Passport.objects.create(inn='21212200012345', id_card='ID1234567', employee=alex)
passport2 = Passport.objects.create(inn='21210198912345', id_card='ID1234568', employee=kuban)
passport3 = Passport.objects.create(inn='21212200012345', id_card='ID1234569', employee=victor)
passport4 = Passport.objects.create(inn='19999999912345', id_card='ID1234560', employee=altynai)

passport2.delete()
kuban.delete()

lms = WorkProject.objects.create(project_name='LMS')

lms.members.set([alex, altynai, victor], through_defaults={'date_joined': '2021-12-20'})

lms.members.remove(alex)

janybek = Employee.objects.create(name='Janybek', birth_date='1989-6-4',
                               position='logist', salary=900, work_experience='2012-5-12')
passport5 = Passport.objects.create(inn='19999999912340', id_card='ID1234568', employee=janybek)

lms.members.add(janybek, through_defaults={'date_joined': '2022-9-9'})

aidar = Client.objects.create(name='Aidar', birth_date='1989-6-4',
                               address='Bishkek', phone_number='0555123456')
aida = Client.objects.create(name='Aida', birth_date='1989-4-4',
                               address='Bishkek', phone_number='0555123459')
evgeniy = Client.objects.create(name='Evgeniy', birth_date='1989-8-4',
                               address='Bishkek', phone_number='0555123450')

nursultan = VIPClient.objects.create(name='Nursultan', birth_date='1991-1-1',
                               address='Bishkek', phone_number='0555123400', donation_amount=2000)

evgeniy.delete()

employees = Employee.objects.all()
for e in employees:
    print(e)

for e in employees:
    print(f'{e.name} {e.passport.inn} {e.passport.id_card}')

projects = WorkProject.objects.all()
for p in projects:
    print(p)

projects = WorkProject.objects.filter(members__name__startswith="Altynai")
print(projects)

clients = Client.objects.all()
for c in clients:
    print(c)

vipclients = VIPClient.objects.all()
for vip in vipclients:
    print(vip)


