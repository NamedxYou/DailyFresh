
from django.conf.urls import url

from app01 import views

urlpatterns = [
    # 设置首页的路由，默认在app/路径下为空时自动进入应用的首页
    url(r'^$', views.index, name='index'),
    # 设置商品详情页面
    url(r'^detail/', views.detail, name='detail'),
    # 设置购物车网页的路由
    url(r'^cart/', views.cart, name='cart'),
    # 这个用于返回购物车数据,便于ajax进行数据渲染
    url(r'^cart_details/', views.cart_details, name='cart_details'),
    # 增加商品到购物车的视图函数，实现前后数据一致
    url(r'^add_goods/', views.add_goods, name='add_goods'),
    # 从购物车减少商品，
    url(r'^minus_goods/', views.minus_goods, name='minus_goods'),
    # 设置下单网页路由
    url(r'^place_order/', views.place_order, name='place_order'),
    # 拿到购物车中选中商品的数据用于下单结算
    url(r'^place_order_data', views.place_order_data, name='place_order_data'),
    # 设置商品列表网页路由
    url(r'^list/', views.list, name='list'),
    # 设置用户中心 -- 个人信息网页路由
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 设置用户中心 -- 订单信息网页路由
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 设置用户中心 -- 收货信息网页路由
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
]
