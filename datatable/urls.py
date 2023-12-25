from django.urls import path,include
from .views import ModelList,model_list
urlpatterns = [
    path('list/',ModelList.as_view()),
    path('modellist/',model_list)
]


