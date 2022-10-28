from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='beneficiaries_app'

urlpatterns = [
    path('', views.index, name='wellcome'),
    path('beneficiary_new/', views.beneficiary_new, name='beneficiary_new'),
    path('beneficiary_edit/<int:beneficiaries_id>/', views.beneficiary_edit, name='beneficiary_edit'),
    path('beneficiary_delete/<int:beneficiaries_id>/', views.beneficiary_delete, name='beneficiary_delete'),
    path('beneficiary_list/', views.beneficiary_list, name='beneficiary_list'),
]