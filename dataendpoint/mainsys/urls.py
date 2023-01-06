from django.urls import path,include
from .views import UploadFileView
from .views import DataAPIView

urlpatterns = [

    path('upload/',UploadFileView.as_view(),name = 'upload-file'),
    path('',DataAPIView.as_view() ,name = 'all-data')

]