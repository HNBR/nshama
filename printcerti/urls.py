from django.urls import path
from .views import CreateNewCertification, DetailCertification

urlpatterns = [
    path("", CreateNewCertification.as_view(), name="create"),
    path("verify/<int:pk>", DetailCertification.as_view(), name="detail")
]
