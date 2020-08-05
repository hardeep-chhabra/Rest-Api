from rest_framework import routers
from rest_api import api_views
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r'projects', api_views.ProjectViewset)
router.register(r'clients', api_views.ClientViewset)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]