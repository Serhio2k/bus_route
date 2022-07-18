from django.urls import path

from towns import views
from towns.views import *


app_name = 'towns'

urlpatterns = [
    path('', TownListView.as_view(), name='home'),
    path('detail/<int:pk>', TownDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TownUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TownDeleteView.as_view(), name='delete'),
    path('add/', TownCreateView.as_view(), name='create')

]
