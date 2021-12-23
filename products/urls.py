from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.products_list, name='list'),
    path('<int:product_id>/', views.products_detail, name='detail'),
    path('<int:product_id>/question/create/', views.question_create, name='create_question'),
]