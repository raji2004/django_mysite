from django.contrib import admin
from django.urls import path,include
from . import views  # Replace 'myapp' with the name of your Django app

urlpatterns = [
    path('', views.index, name='index'),  # Define a view named 'home' to handle the root path
    path('polls/', include('polls.urls')),  # Include URL patterns for other apps
    path('admin/', admin.site.urls),

]