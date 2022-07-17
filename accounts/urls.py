from django.urls import path

from .views import SignUpForm

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpForm.as_view(), name='signup')
]
