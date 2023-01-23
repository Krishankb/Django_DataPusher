"""DataPusher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dataPusher.views import AccountViewSet, DestinationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dataPusher.DataHandlerView import DataHandlerView
from dataPusher.views import AccountViewSet, DestinationViewSet, AccountDestinationView

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('webhook/', include('webhook.urls')),
    path('destinations/<int:account_id>/', AccountDestinationView.as_view()),
    path('server/incoming_data/', DataHandlerView.as_view()),
    path('', include(router.urls))
]
