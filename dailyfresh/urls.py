"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static

from dailyfresh import settings

urlpatterns = [
    # 后台站点管理应用路由系统
    url(r'^admin/', include('admin.urls', namespace='admin')),
    # 将应用app01的路由与项目的路由系统进行关联，并附加命名空间，方便应用内部路由的调用
    url(r'^app/', include('app01.urls', namespace='app')),
    # 将运用 user的路由与项目的路由系统相关联，本应用主要处理与用户信息相关的视图处理，比如登录、注册、注销
    url(r'^user/', include('user.urls', namespace='user')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
