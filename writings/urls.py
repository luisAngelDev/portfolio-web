from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . views import home_publication, details

urlpatterns = [
    path('', home_publication, name='home_publication'),
    path('details/<int:id>', details, name='publication_details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)