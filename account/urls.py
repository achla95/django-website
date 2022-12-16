from django.conf import settings
from django.urls import path
from .views import SignUpView, upload_file

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("upload_file/" , upload_file, name="upload_file"),
] 


#password user achla : Pa$$w0rd&*