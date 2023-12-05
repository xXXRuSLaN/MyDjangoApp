"""
URL configuration for DjangoPulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pulse.views import index, LoginPage, Register
from api.views import GetPulsInfo, GetMathsPuls, SetPulsVote, GetVotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='mainPage'),
    path('api/puls/', GetPulsInfo.as_view(), name='api_get_puls_info'),
    path('api/math/', GetMathsPuls.as_view(), name='api_get_math'),
    path('api/puls/vote/', SetPulsVote.as_view(), name='api_set_puls_vote'),
    path('api/puls/count/', GetVotes.as_view(), name='api_get_puls_vote_score'),
    path('login/', LoginPage.as_view(), name='login'),
    path('', index, name='sozdat'),
    path('register/', Register.as_view(), name='register')
]

