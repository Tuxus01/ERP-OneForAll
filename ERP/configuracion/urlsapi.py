from rest_framework import routers

from .viewsets import *


router = routers.SimpleRouter()
router.register('Company', CompanyViewSet)
router.register('Branch', BranchViewSet)
router.register('Category', CategoryViewSet)
router.register('Status', StatusNamesViewSet)
router.register('Warehouse', WarehouseViewSet)
router.register('SubCategory', SubCategoryViewSet)
router.register('Units', UnitsViewSet)
router.register('Colors', ColorsViewSet)
router.register('Component', ComponentViewSet)
router.register('Bins', BinsViewSet)
router.register('Materials', MaterialsViewSet)
router.register('Adrresses', AdrressesViewSet)
router.register('PurchaseType', PurchaseTypeViewSet)
router.register('Currency', CurrencyViewSet)
router.register('PurchaseOrders', PurchaseOrdersyViewSet)
router.register('PurchaseOrderDetail', PurchaseOrderDetailViewSet)
router.register('Container', ContainerViewSet)
router.register('Users', UserViewSet)


urlpatterns = router.urls