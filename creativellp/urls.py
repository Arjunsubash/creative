from django.urls import path
from . import views
from django.conf.urls.static import static
from creative import settings

urlpatterns = [
    path('',views.Home,name='Home'),
    path('aboutus',views.Aboutus,name='Aboutus'),
    path('contact',views.Contact,name='Contact'),
    path('portfolio',views.Portfolio,name='Portfolio'),
    
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)