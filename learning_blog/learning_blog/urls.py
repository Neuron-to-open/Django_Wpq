"""
URL configuration for learning_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# 页面跳转 配合 views
from django.contrib import admin
from django.urls import path

import app01
from app01 import views
import Department
from Department import views

urlpatterns = [

    path('something/', app01.views.something),
    # 案例：用户管理
    path('info/list/', app01.views.info_list),
    path('info/add/', app01.views.info_add),
    path('info/delete/', app01.views.info_delete),

    # 案例 员工管理
    path('depart/list/', Department.views.depart_list),
    path('depart/add/', Department.views.depart_add),
    path('depart/delete/', Department.views.depart_delete),
    path('depart/<int:nid>/edit/', Department.views.depart_edit),
    # path('depart/edit/', Department.views.depart_edit),
    path('user/list/', Department.views.user_list),
    path('user/add/', Department.views.user_add),

    path('user/model/form/add/', Department.views.user_model_form_add),
]
