
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('divisions/', views.divisions_index, name ='index')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
