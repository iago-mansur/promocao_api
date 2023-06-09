from api.views import EmpresaViewSet, LojaViewSet, PromocaoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('empresas', EmpresaViewSet)
router.register('lojas', LojaViewSet)
router.register('promocoes', PromocaoViewSet)