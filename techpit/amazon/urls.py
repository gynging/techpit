from django.urls import path
from . import views
from django.contrib import admin

app_name = 'amazon'

urlpatterns = [
    path('lp/', views.Lp.as_view(),name = 'lp'),
    path('items/', views.ItemList.as_view(), name = 'item_list'), # この行を追加
]