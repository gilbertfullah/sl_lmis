from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("jet/", include('jet.urls', 'jet')),
    #path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('lmi/', include('lmi.urls')),
    path('jobs/', include('jobs.urls')),
    path('news_and_events/', include('news_and_events.urls')),
    path('career_dev/', include('career_dev.urls')),
    path('sl_lmis/', include('about.urls')),
    path('training_programs/', include('training_programs.urls')),
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
