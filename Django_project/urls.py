"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # เพิ่ม include
from myapp.views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView  # แทนที่ your_app_name ด้วยชื่อแอปของคุณ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ItemListView.as_view(), name='item_list'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/create/', ItemCreateView.as_view(), name='item_create'),
    path('items/update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    path('items/delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]


