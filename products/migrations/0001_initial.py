# Generated by Django 4.0 on 2021-12-21 02:08

from django.db import migrations, models
import django.db.models.deletion

from products.models import Product, ProductReal


def gen_data(apps, schema_editor):
    # 마켓 1
    # 상품 1

    product = Product(market_id=1, name="블라우스1", display_name="연예인 블라우스1", price=20000, sale_price=18000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=1, name="블라우스3", display_name="연예인 블라우스3", price=20000, sale_price=18000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=1, name="블라우스3", display_name="연예인 블라우스3", price=20000, sale_price=18000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()



    product = Product(market_id=1, name="원피스1", display_name="인스타여신원피스1", price=10000, sale_price=9000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()



    # 상품 2
    product = Product(market_id=1, name="원피스2", display_name="인스타여신원피스2", price=20000, sale_price=19000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 상품 3
    product = Product(market_id=1, name="원피스3", display_name="인스타여신원피스3", price=30000, sale_price=29000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 마켓 2
    # 상품 1

    product = Product(market_id=2, name="니트1", display_name="아이돌 니트1", price=15000, sale_price=13000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=2, name="니트2", display_name="아이돌 니트2", price=15000, sale_price=13000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=2, name="니트3", display_name="아이돌 니트3", price=15000, sale_price=13000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=2, name="티셔츠1", display_name="인스타여신티셔츠1", price=10000, sale_price=9000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 상품 2
    product = Product(market_id=2, name="티셔츠2", display_name="인스타여신티셔츠2", price=20000, sale_price=19000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 상품 3
    product = Product(market_id=2, name="티셔츠2", display_name="인스타여신티셔츠3", price=30000, sale_price=29000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드", is_hidden=True).save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 마켓 3
    # 상품 1

    product = Product(market_id=3, name="스커트1", display_name="인스타 셀럽 스커트1", price=30000, sale_price=27000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=3, name="스커트2", display_name="인스타 셀럽 스커트2", price=30000, sale_price=27000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=3, name="스커트3", display_name="인스타 셀럽 스커트3", price=30000, sale_price=27000)
    product.save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    product = Product(market_id=3, name="바지1", display_name="신사바지1", price=10000, sale_price=9000, is_hidden=True)
    product.save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 상품 2
    product = Product(market_id=3, name="바지2", display_name="신사바지2", price=10000, sale_price=9000)
    product.save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="RED",
                option_2_display_name="감성레드", is_sold_out=True, stock_quantity=10).save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="BLUE",
                option_2_display_name="감성블루").save()

    # 상품 3
    product = Product(market_id=3, name="바지3", display_name="신사바지3", price=10000, sale_price=9000)
    product.save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="RED",
                option_2_display_name="감성레드", is_sold_out=True).save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="RED",
                option_2_display_name="감성레드").save()
    ProductReal(product=product, option_1_name="24", option_1_display_name="24", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="26", option_1_display_name="26", option_2_name="BLUE",
                option_2_display_name="감성블루").save()
    ProductReal(product=product, option_1_name="28", option_1_display_name="28", option_2_name="BLUE",
                option_2_display_name="감성블루").save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='삭제날짜')),
                ('name', models.CharField(max_length=100, verbose_name='상품명(내부용)')),
                ('display_name', models.CharField(max_length=100, verbose_name='상품명(고객용)')),
                ('price', models.PositiveIntegerField(verbose_name='권장판매가')),
                ('sale_price', models.PositiveIntegerField(verbose_name='실제판매가')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('category_id', models.PositiveIntegerField(default=0, verbose_name='카테고리번호(추후설계)')),
                ('hit_count', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('review_count', models.PositiveIntegerField(default=0, verbose_name='리뷰수')),
                ('review_point', models.PositiveIntegerField(default=0, verbose_name='리뷰평점')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='markets.market')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('option_1_type', models.CharField(default='SIZE', max_length=10, verbose_name='옵션1 타입')),
                ('option_1_name', models.CharField(max_length=50, verbose_name='옵션1 이름(내부용)')),
                ('option_1_display_name', models.CharField(max_length=50, verbose_name='옵션1 이름(고객용)')),
                ('option_2_type', models.CharField(default='COLOR', max_length=10, verbose_name='옵션2 타입')),
                ('option_2_name', models.CharField(max_length=50, verbose_name='옵션2 이름(내부용)')),
                ('option_2_display_name', models.CharField(max_length=50, verbose_name='옵션2 이름(고객용)')),
                ('option_3_type', models.CharField(blank=True, default='', max_length=10, verbose_name='옵션3 타입')),
                ('option_3_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(내부용)')),
                ('option_3_display_name',
                 models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(고객용)')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('add_price', models.IntegerField(default=0, verbose_name='추가가격')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='재고개수, 품절일때 유용함')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.RunPython(gen_data),
    ]
