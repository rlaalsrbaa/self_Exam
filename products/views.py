from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages

# Create your views here.
from products.models import Product, ProductReal
from questions.models import Question


def products_list(request: HttpRequest):
    product_list = Product.objects.order_by('-id')
    return render(request, 'products/product_list.html', {
        'product_list': product_list,
    })

def products_detail(request: HttpRequest, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    product_reals = product_detail.product_reals.all()
    questions = Question.objects.filter(object_id=product_id)
    return render(request, 'products/product_detail.html', {
        'product_detail': product_detail,
        'product_reals': product_reals,
        'questions': questions,
    })

def question_create(request: HttpRequest, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product_content_type = ContentType.objects.get_for_model(product)
        if request.POST.get('body') == '':
            return redirect('products:detail', product_id)
        question = Question(user_id=1, content_type=product_content_type, object_id=product.id, body=request.POST.get('body'),
                            reg_date=timezone.now()).save()
        messages.warning(request, "작성완료.")
        return redirect('products:detail',product_id)
    else:
        product_detail = get_object_or_404(Product, pk=product_id)
        product_reals = product_detail.product_reals.all()
        questions = Question.objects.filter(object_id=product_id)
        return render(request, 'products/question_form.html', {
            'product_detail': product_detail,
            'product_reals': product_reals,
            'questions': questions,
        })
def question_delete(request: HttpRequest, product_id,question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    product_id = product_id
    messages.warning(request, "삭제완료.")
    return redirect('products:detail',product_id)

def question_modify(request: HttpRequest, product_id,question_id):
    if request.method == 'POST':
        if request.POST.get('body') == '':
            return redirect('products:detail', product_id)
        question = Question.objects.get(id=question_id)
        question.body=request.POST.get('body')
        question.update_date=timezone.now()
        question.save()
        product_id = product_id
        messages.warning(request, "수정완료.")
        return redirect('products:detail', product_id)
    else:
        product_detail = get_object_or_404(Product, pk=product_id)
        product_reals = product_detail.product_reals.all()
        questions = Question.objects.filter(object_id=product_id)

        return render(request, 'products/question_form.html', {
            'product_detail': product_detail,
            'product_reals': product_reals,
            'questions': questions,
        })
