# Generated by Django 4.0 on 2022-01-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='test', max_length=100, verbose_name='이름'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '남성'), ('female', '여성')], max_length=6, verbose_name='성별'),
        ),
    ]
