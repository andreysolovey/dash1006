from django.contrib import admin
from django.urls import path
from adw import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('data', views.Output.as_view(), name='data')
]

