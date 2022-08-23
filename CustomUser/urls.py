
from django.contrib import admin
from django.urls import path, include

from customUser import views as customUserViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('users/', customUserViews.CustomUserView)

]
