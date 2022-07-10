from django.urls import path

from towns import views
from towns.views import *
app_name = 'towns'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', TownDetailView.as_view(), name='detail')
]
