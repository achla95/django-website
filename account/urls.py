from django.urls import path
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]


#password user achla : Pa$$w0rd&*