from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView , PasswordResetView , \
    PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
from django.urls import path , re_path
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

]
