from django.urls import path, re_path
from basic_app import views

#TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns=[
    re_path(r'register/$',views.register,name='register'),
    path('user_login/',views.user_login,name="user_login")
]
