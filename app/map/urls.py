from django.urls import path

from map import views
from map.views import MapTemplateView

urlpatterns = [
    path('odh_records/', views.odh_record_dataset, name='odh_record_dataset'),
    path('', MapTemplateView.as_view(), name='map'),
]
