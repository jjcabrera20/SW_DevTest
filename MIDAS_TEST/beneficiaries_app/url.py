from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='beneficiaries_app'

urlpatterns = [
    path('', views.index, name='wellcome'),
    #path('persona_new/', views.persona_new, name='persona_new'),
    #path('persona_edit/<int:persona_id>/', views.persona_edit, name='persona_edit'),
    #path('persona_list/', views.persona_list, name='persona_list'),
]