from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path("jet/", include('jet.urls', 'jet')),
    #path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #path("", include('admin_adminlte.urls')),
    path('accounts/', include('accounts.urls')),
    path('lmi/', include('lmi.urls')),
    path('jobs/', include('jobs.urls')),
    path('news_and_events/', include('news_and_events.urls')),
    path('career_dev/', include('career_dev.urls')),
    path('training_programs/', include('training_programs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('resources/', include('resources.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
