from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.shortcuts import redirect

from django.conf import settings


def temp_account_redirect(request):
    return redirect('/')


urlpatterns = [
    path('', include('src.account.urls')),
    path('api/', include('src.api.urls')),
    path('account/', temp_account_redirect),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
