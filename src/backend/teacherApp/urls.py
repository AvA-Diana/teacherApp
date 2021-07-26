from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('BackendAccount', views.BackendAccountView)
router.register('Class', views.ClassView)
router.register('Manager', views.ManagerView)
router.register('FrontAccount', views.FrontAccountView)
router.register('People', views.PeopleView)
router.register('ChoiceQuestion', views.ChoiceQuestionView)
router.register('Media', views.MediaView)

urlpatterns = [
    path('', include(router.urls)),
]
