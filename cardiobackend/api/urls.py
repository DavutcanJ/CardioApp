from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularAPIView
urlpatterns= [
    path("cardiouser/",views.UserListCreate.as_view(),name="user-view-create"),
    path("cardiouser/<int:pk>/",
         views.UserListRetrieveUpdateDestroy.as_view(),name="update"),
    path("cardiouser/getdeseaserate/<int:pk>/",
         views.UserDiseaseRate.as_view(),name="desease"),
    path("getcardiodata/",views.UserDiseaseData.as_view(),name="data  "),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]