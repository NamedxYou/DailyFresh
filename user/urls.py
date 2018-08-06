
from django.conf.urls import url

from user import views

urlpatterns = [
    # 设置首页的路由，默认在app/路径下为空时自动进入应用的首页
    url(r'^$', views.user_center, name='user_center'),
    # 设置注册页面的路由
    url(r'^register/', views.register, name='register'),
    # 设置登录页面的路由
    url(r'^login/', views.login, name='login'),

]