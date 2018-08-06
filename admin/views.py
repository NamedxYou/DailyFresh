from django.http import JsonResponse
from django.shortcuts import render

from app01.models import Goods


def index(request):

    if request.method == 'GET':
        return render(request, 'back_management/index.html')


def product_list(request):

    if request.method == 'GET':
        data = {}
        products = Goods.objects.all()
        data['products'] = products
        # 拿到Goods的所有字段及字段名,结果是包含（<字段：字段名>）的元组
        fields = Goods._meta._get_fields()
        # 拿到所有的字段名,去掉反查外键、外键
        fieldnames = []
        for i in range(1,len(fields)-1):
            j = fields[i].name
            fieldnames.append(j)
        data['fieldnames'] = fieldnames
        return render(request, 'back_management/product_list.html', data)

    if request.method == 'POST':
        field = request.POST.get('field')
        content = request.POST.get('content')
        products = Goods.objects.filter(field.like(content))
        data = {}
        data['products'] = products
        return render(request, 'back_management/product_list.html', data)


def product_detail(request):

    if request.method == 'GET':
        return render(request, 'back_management/product_detail.html')


def recycle_bin(request):

    if request.method == 'GET':
        products = Goods.objects.filter(is_deleted=True)
        return render(request,'back_management/recycle_bin.html',{'products': products})


def order_list(request):

    if request.method == 'GET':
        return render(request, 'back_management/order_list.html')


def order_detail(request):

    if request.method == 'GET':
        return render(request, 'back_management/order_detail.html')


def user_list(request):

    if request.method == 'GET':
        return render(request, 'back_management/user_list.html')


def user_detail(request):

    if request.method == 'GET':
        return render(request, 'back_management/user_detail.html')


def user_rank(request):
    if request.method == 'GET':
        return render(request, 'back_management/user_rank.html')


def adjust_funding(request):

    if request.method == 'GET':
        return render(request, 'back_management/adjust_funding.html')


def setting(request):

    if request.method == 'GET':
        return render(request, 'back_management/setting.html')


def express_list(request):

    if request.method == 'GET':
        return render(request, 'back_management/express_list.html')


def pay_list(request):

    if request.method == 'GET':
        return render(request, 'back_management/pay_list.html')


def discharge_statistic(request):

    if request.method == 'GET':
        return render(request, 'back_management/discharge_statistic.html')


def sales_volume(request):

    if request.method == 'GET':
        return render(request, 'back_management/sales_volume.html')

