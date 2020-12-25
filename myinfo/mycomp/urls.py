from django.urls import path

from . import views
app_name = 'mycomp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.index, name='info')
]