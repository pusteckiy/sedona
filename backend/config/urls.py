from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.shortcuts import render

from django.conf import settings


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('', index, name='index'),
    path('api/', include('src.api.urls')),
    path('shop/', include('src.shop.urls')),
    path('account/', include('src.account.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
