from django.urls import path

from file_processing import views

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='upload_file'),
    path('view_file/', views.file_view, name='file_view')
]