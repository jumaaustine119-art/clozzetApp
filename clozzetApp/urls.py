from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('products/', views.ProductView.as_view(),name='products'),
    path('register/',views.UserRegistrationView.as_view(),name='user')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
