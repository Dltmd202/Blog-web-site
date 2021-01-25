from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)