from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='beneficiaries_app'

urlpatterns = [
    path('', views.index, name='wellcome'),
    path('beneficiary_new/', views.beneficiary_new, name='beneficiary_new'),
    #path('persona_edit/<int:persona_id>/', views.persona_edit, name='persona_edit'),
    path('beneficiary_list/', views.beneficiary_list, name='beneficiary_list'),
]