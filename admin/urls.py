
from django.conf.urls import url

from admin import views

urlpatterns = [
    # 设置首页的路由，默认在app/路径下为空时自动进入应用的首页
    url(r'^$', views.index, name='index'),
    # 设置后台管理商品列表的页面路由
    url(r'^product_list/', views.product_list, name='product_list'),
    # 设置后台管理商品详情的页面路由
    url(r'^product_detail/', views.product_detail, name='product_detail'),
    # 设置后台管理商品回收站的页面路由
    url(r'^recycle_bin/', views.recycle_bin, name='recycle_bin'),
    # 设置订单列表页面路由
    url(r'^order_list/', views.order_list, name='order_list'),
    # 设置订单详情页面路由
    url(r'^order_detail/', views.order_detail , name='order_detail'),
    # 设置用户列表页面路由
    url(r'^user_list/', views.user_list, name='user_list'),
    # 设置用户详情页面路由
    url(r'^user_detail/', views.user_detail, name='user_detail'),
    # 设置用户等级页面路由
    url(r'^user_rank/', views.user_rank, name='user_rank'),
    # 设置会员资金管理页面路由
    url(r'^adjust_funding/', views.adjust_funding, name='adjust_funding'),
    # 设置站点管理示例页面路由
    url(r'^setting/', views.setting, name='setting'),
    # 设置配送方式列表页面路由
    url(r'^express_list/', views.express_list, name='express_list'),
    # 设置支付方式列表页面路由
    url(r'^pay_list/', views.pay_list, name='pay_list'),
    # 设置流量统计页面路由
    url(r'^discharge_statistic/', views.discharge_statistic, name='discharge_statistic'),
    # 设置销售额统计页面路由
    url(r'^sales_volume/', views.sales_volume, name='sales_volume'),
]