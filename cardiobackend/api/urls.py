from django.urls import path
from . import views

urlpatterns= [
    path("cardiouser/",views.UserListCreate.as_view(),name="user-view-create"),
    path("cardiouser/<int:pk>/",
         views.UserListRetrieveUpdateDestroy.as_view(),name="update"),
    path("cardiouser/getdeseaserate/<int:pk>/",
         views.UserDiseaseRate.as_view(),name="desease")
]