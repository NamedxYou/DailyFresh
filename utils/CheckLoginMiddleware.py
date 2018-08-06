"""
request 处理中间件
创建用户登录认证的中间件，对需要登录才能访问的页面进行保护
未登录情况下进行必要的页面跳转

在 settings 文件中配置 这个中间件 后页面将会自动进行路由解析处理
"""
from datetime import datetime

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserTicket


class CheckLoginMiddleware(MiddlewareMixin):
    # 处理请求
    def process_request(self,request):
        # 当用户访问下面的路由的时候不进行跳转
        path = ['/user/login/','/user/register/','/app/']
        if request.path in path:
            # return None就是不进行url跳转
            return None

        # 查看在 cookies中是否有 ticket 存在，以判断用户是否登录
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            # 没有 ticket 值跳转到 login 页面
            return HttpResponseRedirect(reverse('user:login'))

        # 拿到ticket 值后通过userticket数据表查询到对应的user, 使用get()拿不到或不止一个会报错，所以使用filter
        user = UserTicket.objects.filter(ticket=ticket).first()
        if not user:
            # 拿不到 user 说明数据库中不存在对应的ticket值，
            # 用户未登录或创建了虚假 ticket 模拟登录
            return HttpResponseRedirect(reverse('user:login'))

        # 拿到user 之后再判断 ticket 是否已经过期，这儿的out_time 已经使用 getter 处理了
        if user.out_time.replace(tzinfo=None) < datetime.now():
        # if user.out_time.replace(tzinfo=None) < datetime.now():
            # 过期时刻已经小于当前时刻，说明用户已经很久没有访问网页了，应该将网页自动跳转到登录页
            # 避免他人利用用户登录后未退出窃取用户信息，将 userticket 数据库对应 user 数据清空
            user.delete()
            return HttpResponseRedirect(reverse('user:login'))
        # 访问页面的用户对象就是 ticket 数据表 字段user对应的user对象（User）
        request.user = user.user
        return None
