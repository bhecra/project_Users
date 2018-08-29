from django.urls import path, include
from rest_framework import routers
from webservices.views import *
from tienda import views as local_views
from posts import views as post_views

router  = routers.DefaultRouter()
router.register(r'profile',producto_viewset)
router.register(r'user',user_viewset)


urlpatterns = [

    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framewrk')),    
    
]