from api.views import EmpresaViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api', EmpresaViewSet)