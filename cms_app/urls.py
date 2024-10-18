from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.site_list, name='site_list'),
    path('sites/<int:site_id>/items/', views.item_list, name='item_list'),
    path('items/<int:item_id>/process/', views.process_detail, name='process_detail'),
]
