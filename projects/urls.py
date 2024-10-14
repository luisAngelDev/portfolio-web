from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import projects, details
#from .import views

urlpatterns = [
    #path('', views.main, name='main'),
    #path('projects/', views.projects, name='projects'),
    path('', projects, name='projects'),
    path('details/<int:id>', details, name='details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)