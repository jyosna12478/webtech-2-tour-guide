from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
	path('',include('accounts.urls'))
    #path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
	
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

