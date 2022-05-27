from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    path('', views.loginPage, name="login"),
    path('admin', admin.site.urls),
    path('signup', views.signup, name = "signup"),
    path('homepage', views.homepage, name= "homepage"),
    path('logout', views.logOut, name="logout"),
    path('search/<str:pk>', views.search, name="search"),
    path('<str:pk>', views.profile, name = "profile" ),
    
]