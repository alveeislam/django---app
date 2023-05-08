from django.contrib import admin
from django.urls import path, re_path

# from learning_logs import views
from learning_logs.views import *

urlpatterns = [
    path('', home, name = "home"),
    path('topics/', topics, name = 'topics'),
    path('admin/', admin.site.urls),
    
    

]