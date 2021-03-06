"""map_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from map_project import settings
from map_project.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='home'),
    path('map/', include('map.urls')),
    path('upload_file/', include('file_processing.urls')),
    path('accounts/', include('accounts.urls')),
    path('statistic_1/', TemplateView.as_view(template_name='statistic/chart_1.html'), name='chart_1'),
    path('statistic_2/', TemplateView.as_view(template_name='statistic/chart_2.html'), name='chart_2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
