# Generated by Django 4.0 on 2021-12-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='100px * 100px 크기의 gif/png/jpg 이미지를 업로드해주세요.', upload_to='accounts/avatar/%Y/%m/%d', verbose_name='아바타'),
        ),
    ]
