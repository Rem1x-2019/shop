# ����ʵ��� http://127.0.0.1:8000/ ��·��������Ŀû�����ø�·���� URL��
# ���������Ϊ��·�����һ����ת����ҳ��

# 1. �޸� ModularEcommerceHTMX/urls.py �ļ����£�

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('store/', permanent=False)),  # ������У���ת�� /store/
    path('admin/', admin.site.urls),
    path('cart/', include('apps.cart.urls')),
    path('checkout/', include('apps.checkout.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('modules/', include('apps.modules.urls')),
    path('store/', include('apps.store.urls')),  # ȷ������ store Ӧ�õ�·��
]

# 2. ȷ�� apps.store.urls �����Ҷ����� URL patterns��������ҳ��
# 3. ������������
# python manage.py runserver

# ���� http://127.0.0.1:8000/ ���Զ���ת�� http://127.0.0.1:8000/store/
