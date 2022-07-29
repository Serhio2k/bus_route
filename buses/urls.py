from django.urls import path


from buses.views import *


app_name = 'buses'

urlpatterns = [
    path('', BusListView.as_view(), name='home'),
    path('detail/<int:pk>', BusDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BusUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BusDeleteView.as_view(), name='delete'),
    path('add/', BusCreateView.as_view(), name='create')

]
