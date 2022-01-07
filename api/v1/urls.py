from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Index.as_view()),
    path('get_token',views.ViewToken.as_view()),
    path('get_film',views.GetFilm.as_view()),
    path('get_film_url',views.GetFilmUrl.as_view())

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)