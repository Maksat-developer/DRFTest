
from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns_swagger
from .api import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
    

] + urlpatterns_swagger

