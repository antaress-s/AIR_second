from django.contrib import admin
from django.urls import path, include
from pandasdemo import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.pandasdemo_view.as_view(), name="api"),
    path('main/', views.main.home, name='osnova'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('csv_bef/', views.main.csv_bef),
    path('csv_del/', views.main.csv_del),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),
]
