from django.urls import path
from .views import ParagraphList, WordSearch, MyTokenObtainPairView, getuser, registeruser
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
   
    path('paragraph/', ParagraphList.as_view(), name='paragraph-list'),
    path('word/search/<str:word>/', WordSearch.as_view(), name='word-search'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/getuser/',getuser,name='getuser'),
    path('api/registeruser/',registeruser,name='registeruser'),
]
