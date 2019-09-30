from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from crinsp.forms import LoginForm
from django.contrib.auth.decorators import login_required



urlpatterns =[
    path('login',views.user_login,name='user_login'),
    path('',views.home,name='home'),
    path('testing',(login_required(login_url='/crinsp/login'))(views.TestingCreateView.as_view()),name='testing'),
    path('status',views.status,name='status'),
    path ('logout',LogoutView.as_view(next_page='user_login'),name="logout"),
    path('password',views.change_password,name='changepassword' )
]