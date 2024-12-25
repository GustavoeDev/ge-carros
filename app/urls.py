from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),                   
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('cars/details/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/details/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)