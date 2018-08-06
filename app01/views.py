from django.http import JsonResponse
from django.shortcuts import render

from app01.models import GoodsType, Goods, Cart
from user.models import ReceiveDetail


def index(request):

    if request.method == 'GET':
        data = {}
        goods_types = GoodsType.objects.all()
        fruits = Goods.objects.filter(goodstype=1)
        seafoods = Goods.objects.filter(goodstype=2)
        data['goods_types'] = goods_types
        data['fruits'] = fruits
        data['seafoods'] = seafoods
        return render(request, 'app/index.html', data)


def list(request):

    if request.method == 'GET':
        return render(request, 'app/list.html')
    if request.method == 'POST':
        return ''


def detail(request):

    if request.method == 'GET':
        id = request.GET.get('id')
        product = Goods.objects.get(id=id)
        data = {}
        data['product'] = product
        return render(request, 'app/detail.html', data)


def cart(request):

    if request.method == 'GET':
        # 拿到当前发送请求的用户
        user = request.user
        data = {}
        # 查询所有与当前用户关联的购物车信息
        carts = Cart.objects.filter(user=user)
        # 判断购物车是否为空
        if carts:
            # 获取购物车所有详细信息[{'id':1,'name':2},{'id':3,'name':4},]形式
            cart_details = [cart.to_dict() for cart in carts]
            data['cart_details'] = cart_details
        else:
            data['cart_details'] = ''
        return render(request, 'app/cart.html',data)

    if request.method == 'POST':
        user = request.user
        goods_num = request.POST.get('goods_num')
        goods_id = request.POST.get('goods_id')
        cart = Cart()
        cart.user = user
        cart.num = goods_num
        cart.goods = Goods.objects.get(id=goods_id)
        cart.save()

        return JsonResponse({'code':'200'})


# 用独立的视图函数返回购物车的数据处理
def cart_details(request):

    if request.method == 'GET':
        # 拿到当前发送请求的用户
        user = request.user
        data = {}
        # 查询所有与当前用户关联的购物车信息
        carts = Cart.objects.filter(user=user)
        # 判断购物车是否为空
        if carts:
            # 获取购物车所有详细信息[{'id':1,'name':2},{'id':3,'name':4},]形式
            cart_details = [cart.to_dict() for cart in carts]
            data['cart_details'] = cart_details
            # 状态码 200 表示请求成功拿到数据
            data['code'] = '200'
        else:
            # 状态码 1001 表示数据为空
            data['code'] = '1001'
        return JsonResponse(data)


# 购物车添加商品视图函数，使前端数据与后端数据同步
def add_goods(request):

    if request.method == 'POST':
        # user = request.user
        id = request.POST.get('id')
        goods_num = request.POST.get('goods_num')
        cart = Cart.objects.filter(id=id).first()
        data = {}
        if cart:
            cart.num = goods_num
            cart.save()
            data['code'] = '200'
        else:
            data['code'] = '1001'

    return JsonResponse(data)


# 从购车减少商品，实现前后数据一致
def minus_goods(request):

    if request.method == 'POST':
        id = request.POST.get('id')
        goods_num = request.POST.get('goods_num')
        cart = Cart.objects.filter(id=id).first()
        data = {}
        if cart:
            cart.num = goods_num
            cart.save()
            data['code'] = '200'
        else:
            data['code'] = '1001'

    return JsonResponse(data)


def place_order(request):

    if request.method == 'GET':
        # 拿到当前用户
        user = request.user
        # 拿到当前用户的购物车中所有选中的购物车商品
        carts = Cart.objects.filter(user=user,is_selected=True)
        # 判断是否有商品
        data = {}
        if carts:
            # 拿到所有商品详情
            cart_details = [cart.to_dict() for cart in carts]
            data['cart_details'] = cart_details
        else:
            data['cart_details'] = ''

        return render(request, 'app/place_order.html',data)
    if request.method == 'POST':
        return ''


# 拿到数据给 ajax处理渲染
def place_order_data(request):

    if request.method == 'GET':
        user = request.user
        carts = Cart.objects.filter(user=user,is_selected=True)
        data = {}
        if carts:
            cart_details = [cart.to_dict() for cart in carts]
            data['cart_details'] = cart_details
            data['code'] = '200'
        else:
            data['msg'] = '您还没有选择任何商品！'
            data['code'] = '1001'

        return JsonResponse(data)

def user_center_info(request):

    if request.method == 'GET':
        return render(request, 'app/user_center_info.html')
    if request.method == 'POST':
        return ''


def user_center_order(request):

    if request.method == 'GET':
        return render(request, 'app/user_center_order.html')
    if request.method == 'POST':
        return ''


def user_center_site(request):

    if request.method == 'GET':
        user = request.user
        # 拿到与用户关联的、使用过的收货人信息
        receivers = ReceiveDetail.objects.filter(user=user)
        data = {}
        if receivers:
            receivers_details = [receiver.to_dict() for receiver in receivers]
            data['receivers'] = receivers_details
        else:
            data['receivers'] = ''
        return render(request, 'app/user_center_site.html', data)
    if request.method == 'POST':
        return ''





