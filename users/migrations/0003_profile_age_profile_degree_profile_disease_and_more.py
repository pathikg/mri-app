# Generated by Django 4.0.1 on 2022-03-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='profile',
            name='Degree',
            field=models.CharField(default='MBBS', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='Disease',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='license_number',
            field=models.CharField(default='0000', max_length=500),
        ),
    ]