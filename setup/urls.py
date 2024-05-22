from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from example import views
from example.views import (
    ExampleListView,
    ExampleCreateView,
    ExampleUpdateView,
    ExampleDeleteView,
    ExampleCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('example/', include('example.urls')),
    path('docs/', include('documents.urls')),
    path('', include('users.urls')),
    path('users/', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
