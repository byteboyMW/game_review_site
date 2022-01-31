from django.conf.urls import url
from . import views

app_name = 'test'

urlpatterns = [
    url(r'^$', views.TestView.as_view(),name='home'),
]