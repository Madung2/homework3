# Generated by Django 4.0.5 on 2022-06-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_hobby_alter_userprofile_hobby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hobby',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hobby',
            field=models.ManyToManyField(to='user.hobby', verbose_name='취미'),
        ),
    ]
