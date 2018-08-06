
# coding=utf-8
from django.db import models

"""
User: 编号、用户名、用户密码、头像、邮箱 <-- Cart/Order
UserTicket: 编号、ticket、过期时刻 --> User
ReceiveDetail: 编号、接收人姓名、地址、联系方式 --> User
"""

class User(models.Model):

    id = models.AutoField(primary_key=True,db_column='uid',verbose_name='用户id')
    name = models.CharField(max_length=50,unique=True,null=False,db_column='username',verbose_name='用户名')
    password = models.CharField(max_length=255,null=False,db_column='password',verbose_name='用户密码')
    email = models.EmailField(max_length=50,null=False,db_column='email',verbose_name='用户邮箱')
    img = models.ImageField(upload_to='user_icon',null=True,db_column='img',verbose_name='用户头像')

    def Meta(self):
        db_table = 'tb_user'

    # def __str__(self):
    #     return self.name.encode('utf-8')

    # 定义对象方法 to_dict() 获取 json 格式的对象数据
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'img': self.img,
        }


class UserTicket(models.Model):
    id = models.AutoField(primary_key=True,db_column='tid')
    user = models.ForeignKey(User,db_column='uid')  # 关联用户
    ticket = models.CharField(max_length=256,db_column='ticket')   # 密码
    out_time = models.DateTimeField(db_column='out_time')  # 过期时间

    class Meta:
        db_table = 'tb_userticket'

    # # 定义getter方法,获取 out_time 时去掉时区划分
    # @property
    # def out_time(self):
    #     return self.out_time.replace(tzinfo=None)


class ReceiveDetail(models.Model):

    id = models.AutoField(primary_key=True, db_column='udid', verbose_name='用户订单关联详情')
    name = models.CharField(max_length=100, db_column='re_name', verbose_name='收货人姓名')
    address = models.CharField(max_length=1000, verbose_name='收货地址')
    tel = models.CharField(max_length=200, db_column='tel_num', verbose_name='收货人电话')
    user = models.ForeignKey(User, db_column='uid', verbose_name='关联用户')    # 用户可能存在几个收货人信息的情况

    def Meta(self):
        db_table = 'tb_receive_detail'

    def __str__(self):
        return self.name.encode('utf-8')

    # 定义对象方法 to_dict() 获取 json 格式的对象数据
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'tel': self.tel,
            'user': self.user.name,
        }
