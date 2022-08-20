# Generated by Django 3.2 on 2022-08-20 11:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('work_experience', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.client')),
                ('vip_status_start', models.DateField(default=django.utils.timezone.now)),
                ('donation_amount', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('employee.client',),
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('members', models.ManyToManyField(through='employee.Membership', to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=14)),
                ('id_card', models.CharField(max_length=9)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='work_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.workproject'),
        ),
    ]