from os import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('back_end',views.BackEnd.as_view(),name='back_end'),
    path('quotes',views.QuotesView.as_view(),name='quotes'),
    path('backend_q',views.BackEndQuote.as_view(),name='backend_q'),
    path('optimization/razsearch_params',views.BackendRazSearch.as_view(),name='raz_search'),
    path('optimization/first',views.optimization_first,name='backend_q'),
    path('optimization/second',views.optimization_second,name='optimiz_2'),
    path('optimization/second_back',views.BackendSecond.as_view(),name='optimization_second_back'),
    path('fin_otchet',views.fin_otchet,name='fin_otchet'),
    path('fin_otchet/<int:id>', views.fin_detail, name = 'fin_detail'),
    path('fin_otchet/<int:otchet_id>/<int:id>', views.FinOtchetRowsListView.as_view(), name = 'findetails')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)