from os import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('back_end',views.BackEnd.as_view(),name='back_end'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)