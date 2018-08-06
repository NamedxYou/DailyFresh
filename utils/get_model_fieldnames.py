
from app01.models import Goods

# model表示引用的模型名，type表示获取字段名还是verbose_name（自定义名），默认是字段名
def get_model_fieldnames(model, type='name'):

    # 拿到Goods的所有字段及字段名,结果是包含（<字段：字段名>）的元组
    fields = model._meta._get_fields()
    # 拿到所有的字段名,如 id,name等
    fieldnames = []
    for i in range(len(fields)):
        if type == 'name':
            j = fields[i].name
        else:
            j = fields[i].verbose_name
        fieldnames.append(j)

    return fieldnames


