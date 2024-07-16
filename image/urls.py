from django.conf import settings
from django.urls import path
from .views import UploadImageView
from django.conf.urls.static import static

urlpatterns = [
    path('upload_image/',UploadImageView.as_view(),name="UploadImageView")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)