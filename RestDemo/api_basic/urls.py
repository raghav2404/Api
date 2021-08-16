from django.urls import path
from  api_basic.views import *

urlpatterns = [
    path('article/' , article_list),  
    path('detail/<int:pk>/' , article_detail),
]
