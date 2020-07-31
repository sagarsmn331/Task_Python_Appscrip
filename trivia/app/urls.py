from rest_framework.routers import DefaultRouter
from app import views
router = DefaultRouter()
router.register('Name', views.NameViewSet,basename='Name')
router.register('Cricketer', views.CricketerViewSet,basename='Cricketer')
router.register('Flag', views.FlagViewSet,basename='Flag')
router.register('Finish', views.FinishViewSet,basename='Finish')
router.register('Summary', views.SummaryViewSet,basename='Summary')
# router.register('Finish', views.ghjhgViewSet,basename='Finish')
urlpatterns = router.urls