# 你访问的是 http://127.0.0.1:8000/ 根路径，但项目没有配置根路径的 URL。
# 解决方法：为根路径添加一个跳转或首页。

# 1. 修改 ModularEcommerceHTMX/urls.py 文件如下：

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('store/', permanent=False)),  # 添加这行：跳转到 /store/
    path('admin/', admin.site.urls),
    path('cart/', include('apps.cart.urls')),
    path('checkout/', include('apps.checkout.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('modules/', include('apps.modules.urls')),
    path('store/', include('apps.store.urls')),  # 确保包含 store 应用的路由
]

# 2. 确保 apps.store.urls 存在且定义了 URL patterns（例如首页）
# 3. 重启服务器：
# python manage.py runserver

# 访问 http://127.0.0.1:8000/ 将自动跳转到 http://127.0.0.1:8000/store/
