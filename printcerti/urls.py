from django.urls import path
from .views import CreateNewCertification

urlpatterns = [
    path("", CreateNewCertification.as_view(), name="create"),
]
