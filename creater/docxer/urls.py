from .views import UpdateDocxAPIView,openDocxAPI,FirmViewSet,Create_New_Act,ActViewSet,UploadFiles,EmplViewSet
from django.urls import path,include
from rest_framework import routers
router = routers.SimpleRouter()
router.register('Firms' , FirmViewSet,basename = 'Firms')
router.register('Acts' , ActViewSet,basename = 'Firms')
router.register('Empl',EmplViewSet,basename='Empl')

urlpatterns = [
   path('update-docx/' , UpdateDocxAPIView.as_view()),
   path('open_docx',openDocxAPI.as_view()),
   path('createAct/', Create_New_Act.as_view()),
   path('UploadFiles/', UploadFiles.as_view()),

]

urlpatterns+= router.urls

