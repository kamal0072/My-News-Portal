from django.conf import settings
from django.conf.urls.static import static 
# =============================================
from django.contrib import admin
from django.urls import path, include
from news import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('notes/', include("notepad.urls")),
    path('', include("news.urls")),
    path('login/',views.admin_login,name="login"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
