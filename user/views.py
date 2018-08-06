from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from user.models import User, UserTicket
from utils.generate_ticket import generate_ticket


def user_center(request):

    if request.method == 'GET':
        user = request.user
        return render(request, 'app/user_center_info.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'app/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')     # 拿到前端填写的用户名
        password = request.POST.get('password')     # 拿到第一次输入的密码
        email = request.POST.get('email')           # 拿到用户邮箱
        icon = request.FILES.get('icon')              # 拿到用户头像的路径
        data = {}
        if not all([username,password,email]):       # 判断必填信息是否全部输入
            data['msg'] = '请确保信息完善！'
            data['code'] = '1001'
            return render(request, 'app/register.html', data)        # 信息输入不完整，重新返回注册页面，重新填写
        else:
            user = User.objects.filter(name=username).first()       # 判断用户名是否已经被注册
            if not user:        # 用户未注册执行
                User.objects.create(
                    name = username,
                    password = make_password(password),
                    email = email,
                    img = icon
                )
                return HttpResponseRedirect(reverse('user:login'))
            else:       # 用户已注册执行
                data['msg'] = '用户名已经被注册，请输入其他用户名！'
                return render(request, 'app/register.html', data)


def login(request):

    if request.method == 'GET':
        return render(request, 'app/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        data = {}
        if not all([username,password]):    # 信息输入不全：
            data['msg'] = '请确保信息完善！'
            return render(request, 'app/login.html', data)
        else:
            if User.objects.filter(name=username).exists():     # 判断用户名是否存在
                user = User.objects.get(name=username)          # 拿到用户名对应的对象
                if check_password(password, user.password):         # 使用Django自带的密码核验模块验证密码
                    # 利用自定义的函数获取随机固定长度的字符串作为 ticket 值
                    ticket = generate_ticket()
                    # 设置 ticket 的过期时间为 12 小时，out_time 对应当前时刻后延 12h
                    out_time = datetime.now() + timedelta(hours=12)
                    # 拿到跳转的页面，并在其 cookie中设置 ticket 和 out_time
                    res = HttpResponseRedirect(reverse('app:index'))
                    res.set_cookie('ticket', ticket, expires=out_time)
                    # 将关联用户 user, ticket以及过期时刻 out_time保存到userticket 数据表中
                    UserTicket.objects.create(user=user, ticket=ticket, out_time=out_time)
                    # 登录成功跳转到首页
                    return res
                else:
                    data['msg'] = '密码错误，请重新输入！'
                    return render(request, 'app/login.html', data)
            else:
                data['msg'] = '用户名不存在，请确认已注册并输入正确！'
                return render(request, 'app/login.html', data)


def log_out(request):
    if request.method == 'GET':
        # 退出登录，将cookie中的数据清空，访问页面跳转到首页
        request.COOKIES.clear()
        return HttpResponseRedirect(reverse('app:index'))



