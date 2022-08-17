from django.urls import path,include
from.views import *
urlpatterns = [
    path('index/',index_view,name='index'),
    path('middle/',middle_view,name='middle'),
    path('person/',person_view,name='person'),
    path('bloodbank/',bloodbank_view,name='bloodbank'),
    path('list/',list_view,name='list'),
    path('contact/',ContactView.as_view(),name='contact'),
]
