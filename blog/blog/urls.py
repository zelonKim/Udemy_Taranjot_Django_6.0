from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf.urls.static import static
from django.conf import settings
from posts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('posts/', include('posts.urls')),
    path('<int:id>/', views.shortcut),
    path('accounts/', include('accounts.urls')),
    path('users/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'My Blog'
admin.site.index_title = 'The Blog'

