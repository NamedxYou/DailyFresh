
import random
"""
这个函数的目的是生成随机的一串固定长度的字符串，
当用户登录的时候作为 ticket 存入到浏览器的cookie中，
并且在数据库中存入同样的 cookie 用于验证用户是否
是在登录的状态下访问页面内容
"""
def generate_ticket():

    s = '1234567890qazwsxedcrfvtgbyhnujmikolp'
    ticket = ''
    for i in range(15):
        ticket += random.choice(s)
    return ticket

