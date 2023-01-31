"""Polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from poll.views import index, polling_result, sum_total_result_lga, get_loc_id, store_polling_unit_result
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('polling-result/<id>/', polling_result, name='polling-result'),
    path('sum-total/', sum_total_result_lga, name = 'sum-total'),
    path('get-loc/', csrf_exempt(get_loc_id), name = "get-loc"),
    path('store-result/', store_polling_unit_result, name = 'store-result')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

