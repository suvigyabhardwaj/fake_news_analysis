"""fake_news_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

admin.site.site_header = 'Fake News Detector Administration'
admin.site.index_title = 'Fake News Detector Database Details'
admin.site.site_title = 'Fake News Detector Site Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('predict/',views.predict,name='predict'),
    path('real/',views.real,name='real'),
    path('fake/',views.fake,name='fake'),
    path('code/',views.code,name='code'),
    path('history/', views.user_history, name='history'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
]