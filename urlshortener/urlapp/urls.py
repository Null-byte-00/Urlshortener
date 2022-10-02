from . import views
from django.urls import path

app_name = 'urlapp'

urlpatterns = [
    path('', views.MakeUrl.as_view(), name='make_url'),
    path('<slug:urlslug>/', views.redirect_url, name='redirect_url')
]