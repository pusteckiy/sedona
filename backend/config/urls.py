from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from config.settings import STATIC_URL, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('api/', include('src.api.urls')),
    path('', include('src.shop.urls')),
    path('account/', include('src.account.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
