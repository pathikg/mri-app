# Generated by Django 3.1.7 on 2022-02-04 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segmi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab_report',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='lab_report',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='lab_report',
            name='phone',
        ),
    ]
