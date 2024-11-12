from django.urls import path,include
from app.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('curd',views.registerViewSet,basename='user')
urlpatterns = [
    path('',include(router.urls))
]
