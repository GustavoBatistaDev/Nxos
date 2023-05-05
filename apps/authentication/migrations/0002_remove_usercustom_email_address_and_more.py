# Generated by Django 4.2 on 2023-05-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercustom',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='usercustom',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='usercustom',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='usercustom',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
