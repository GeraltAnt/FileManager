from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cms.sitemaps import CMSSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms_app/', include('cms_app.urls')),  # 我们的应用 URL
    path('', include('cms.urls')),  # django CMS URL
]

# 媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)