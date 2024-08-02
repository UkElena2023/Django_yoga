"""
URL configuration for makeyoga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from .sitemaps import AsanaSitemap
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from yoga import views
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'asana': AsanaSitemap,
    }

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'), # главная
    # для поисковиков
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="yoga/robots.txt", content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^yandex_25abbda5384e921f\.html$', TemplateView.as_view(template_name="yoga/yandex_25abbda5384e921f.html")),

    # остальные страницы
    path('about/', views.AboutView.as_view(), name='about'), # стили йоги
    path('advice/', views.AdviceView.as_view(), name='advice'), # советы начинающим
    # Маршруты подключенные из приложения yoga
    path('yoga/', include('yoga.urls')),
    # Маршруты подключенные из приложения users
    path('users/', include('users.urls', namespace='users')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      # другие URL-паттерны
                  ] + urlpatterns
    # Добавляем обработку медиафайлов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Определяем кастомный обработчик 404 ошибки
handler404 = views.PageNotFoundView.as_view()
