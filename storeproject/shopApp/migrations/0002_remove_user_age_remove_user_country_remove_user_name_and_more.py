# Generated by Django 5.1 on 2024-09-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='xyz@email.com', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='wali@example.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='xyz', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='xyz', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='exit', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
