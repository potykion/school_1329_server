from django.urls import path

from school_1329_server.common import views

urlpatterns = (
    path('', views.index_view, name='index'),
    path('login', views.AdminLoginView.as_view(), name='login'),
    path('admin', views.admin_view, name='admin')
)
