from django.urls import path
from . import views

urlpatterns= [
    path("cardiouser/",views.UserListCreate.as_view(),name="user-view-create")
]