# Generated by Django 4.0 on 2021-12-21 02:08

from django.db import migrations, models
import django.db.models.deletion

from markets.models import Market


def gen_master(apps, shema_editor):
    Market(name="언니네옷가게", site_url="https://www.abc1.co.kr", email="test1@test.com", master_id=1).save()
    Market(name="누나네옷가게", site_url="https://www.abc2.co.kr", email="test2@test.com", master_id=2).save()
    Market(name="이모네옷가게", site_url="https://www.abc3.co.kr", email="test3@test.com", master_id=3).save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('name', models.CharField(max_length=100, verbose_name='마켓이름')),
                ('site_url', models.URLField(max_length=100, verbose_name='마켓사이트URL')),
                ('email', models.EmailField(max_length=100, verbose_name='마켓대표이메일')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],

        ),
        migrations.RunPython(gen_master),
    ]
