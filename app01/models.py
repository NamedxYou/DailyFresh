
# coding=utf-8
from django.db import models

# 商品类型信息
from user.models import User, ReceiveDetail

"""
模型逻辑：
User: 编号、用户名、用户密码、头像、邮箱
UserTicket: 编号、ticket、过期时刻 --> User
ReceiveDetail: 编号、接收人姓名、地址、联系方式 --> User
GoodsType: 编号、名称、是否删除该分类(选择性页面展示)
Goods: 编号、名称、图片、价格、是否选中、计量单位、库存、商品介绍 --> GoodsType
Cart: 编号、商品数量、是否选中 --> Goods/User
Order: 编号、下单日期、总计金额、支付状态、运费  --> User/ReceiveDetail
"""

class GoodsType(models.Model):

    id = models.AutoField(primary_key=True, db_column='tid', verbose_name='商品类型编号')
    name = models.CharField(max_length=20, db_column='tname', verbose_name='商品类型名称')
    is_deleted = models.BooleanField(default=False, db_column='is_deleted', verbose_name='是否删除该分类')

    def Meta(self):
        db_table = 'tb_goodstype'

    # def  __str__(self):
    #     return self.name.encode('utf-8')

# 商品详情
class Goods(models.Model):

    id = models.AutoField(primary_key=True, db_column='gid',verbose_name='商品编号')
    name = models.CharField(max_length=20, db_column='gname', verbose_name='商品名称')
    img = models.ImageField(upload_to='media/goods_img/', db_column='gimg', verbose_name='商品图片')
    price = models.DecimalField(max_digits=5, decimal_places=2 , db_column='gprice', verbose_name='商品单价')
    is_deleted = models.BooleanField(default=False, db_column = 'is_deleted', verbose_name='商品是否从购物车中删除')
    unit = models.CharField(max_length=20,default='500g',db_column='gunit', verbose_name='商品计量单位')
    inventory = models.IntegerField(default='999', db_column='ginventory', verbose_name='商品存量')
    detail = models.CharField(max_length=1000,db_column='gdetail', verbose_name='商品详细介绍')
    goodstype = models.ForeignKey(GoodsType, db_column='tid', verbose_name='商品归属类型')

    def Meta(self):
        db_table = 'tb_goods'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': str(self.img),
            'price': self.price,
            'is_deleted': self.is_deleted,
            'unit': self.unit,
            'inventory': self.inventory,
            'detail': self.detail,
            'goodstype': self.goodstype.name,
        }

    # def  __str__(self):
    #     return self.name.encode('utf-8')

# 购物车详情
class Cart(models.Model):

    id = models.AutoField(primary_key=True, db_column='cid', verbose_name='购物车添加商品编号')
    num = models.IntegerField(db_column='cnum', verbose_name='购物车商品数量')
    is_selected = models.BooleanField(default=True, db_column='is_selected', verbose_name='是否选中商品')
    user = models.ForeignKey(User, db_column='uid', verbose_name='购物车用户id')
    goods = models.ForeignKey(Goods, db_column='gid', verbose_name='关联商品id')

    def Meta(self):
        tb_table = 'tb_cart'

    def sum_price(self):
        return (self.goods.price) * self.num

    def to_dict(self):
        return {
            'id': self.id,
            'goods_num': self.num,
            'is_selected': self.is_selected,
            'user_id': self.user.id,
            'goods': self.goods.to_dict(),
            'sum_price': self.sum_price(),
            }

# 订单信息
class Order(models.Model):

    id = models.AutoField(primary_key=True, db_column='oid', verbose_name='订单编号')
    date = models.DateTimeField(auto_now=True, db_column='otime', verbose_name='下单时间')
    total = models.DecimalField(max_digits=6, decimal_places=2, db_column='total', verbose_name='商品总金额')
    freight = models.DecimalField(max_digits=6, decimal_places=2, db_column='freight', verbose_name='运费')
    is_payed = models.BooleanField(default=False, db_column='is_payed', verbose_name='是否已支付')
    user = models.ForeignKey(User, db_column='uid', verbose_name='下单用户')
    cart = models.ForeignKey(Cart, db_column='cid', verbose_name='关联购物车')
    receive_detail = models.ForeignKey(ReceiveDetail, db_column='receive', verbose_name='接收人详情')

    def Meta(self):
        db_table = 'tb_order'


